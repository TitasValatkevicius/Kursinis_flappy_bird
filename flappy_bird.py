import random
from sys import exit

import pygame

GAME_WIDTH = 360
GAME_HEIGHT = 640
FPS = 60

BIRD_WIDTH = 34
BIRD_HEIGHT = 24

PIPE_WIDTH = 64
PIPE_HEIGHT = 512

PIPE_SPAWN_TIME = 1500
GRAVITY = 0.4
JUMP_STRENGTH = -6
PIPE_SPEED = -2
OPENING_SPACE = GAME_HEIGHT // 4

SCORE_FILE = "highscore.txt"


class GameObject:
    def __init__(self, x, y, width, height, image):
        self.rect = pygame.Rect(x, y, width, height)
        self.image = image

    def draw(self, surface):
        surface.blit(self.image, self.rect)


class Bird(GameObject):
    def __init__(self, image):
        super().__init__(
            GAME_WIDTH // 8,
            GAME_HEIGHT // 2,
            BIRD_WIDTH,
            BIRD_HEIGHT,
            image
        )
        self.velocity_y = 0

    def jump(self):
        self.velocity_y = JUMP_STRENGTH

    def update(self):
        self.velocity_y += GRAVITY
        self.rect.y += self.velocity_y

        if self.rect.top < 0:
            self.rect.top = 0
            self.velocity_y = 0

    def reset(self):
        self.rect.x = GAME_WIDTH // 8
        self.rect.y = GAME_HEIGHT // 2
        self.velocity_y = 0


class Pipe(GameObject):
    def __init__(self, x, y, image):
        super().__init__(x, y, PIPE_WIDTH, PIPE_HEIGHT, image)
        self.passed = False

    def update(self):
        self.rect.x += PIPE_SPEED


class PipeFactory:
    @staticmethod
    def create_pair(top_image, bottom_image):
        random_pipe_y = int(
            -PIPE_HEIGHT / 4 - random.random() * (PIPE_HEIGHT / 2)
        )

        top_pipe = Pipe(GAME_WIDTH, random_pipe_y, top_image)
        bottom_pipe = Pipe(
            GAME_WIDTH,
            top_pipe.rect.y + PIPE_HEIGHT + OPENING_SPACE,
            bottom_image
        )

        return top_pipe, bottom_pipe


class ScoreManager:
    def __init__(self, filename):
        self.filename = filename
        self.high_score = self.load_high_score()

    def load_high_score(self):
        try:
            with open(self.filename, "r", encoding="utf-8") as file:
                return float(file.read().strip())
        except (FileNotFoundError, ValueError):
            return 0.0

    def save_high_score(self, score):
        if score > self.high_score:
            self.high_score = score
            with open(self.filename, "w", encoding="utf-8") as file:
                file.write(str(int(self.high_score)))


class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((GAME_WIDTH, GAME_HEIGHT))
        pygame.display.set_caption("Flappy Bird")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont("Comic Sans MS", 32)

        self.background_image = pygame.image.load(
            "assets/flappybirdbg.png"
        )
        self.background_image = pygame.transform.scale(
            self.background_image,
            (GAME_WIDTH, GAME_HEIGHT)
        )

        bird_image = pygame.image.load("assets/flappybird.png")
        bird_image = pygame.transform.scale(
            bird_image,
            (BIRD_WIDTH, BIRD_HEIGHT)
        )

        top_pipe_image = pygame.image.load("assets/toppipe.png")
        top_pipe_image = pygame.transform.scale(
            top_pipe_image,
            (PIPE_WIDTH, PIPE_HEIGHT)
        )

        bottom_pipe_image = pygame.image.load("assets/bottompipe.png")
        bottom_pipe_image = pygame.transform.scale(
            bottom_pipe_image,
            (PIPE_WIDTH, PIPE_HEIGHT)
        )

        self.bird = Bird(bird_image)
        self.top_pipe_image = top_pipe_image
        self.bottom_pipe_image = bottom_pipe_image

        self.pipes = []
        self.score = 0
        self.game_over = False

        self.score_manager = ScoreManager(SCORE_FILE)

        self.create_pipes_timer = pygame.USEREVENT + 1
        pygame.time.set_timer(self.create_pipes_timer, PIPE_SPAWN_TIME)

    def reset(self):
        self.bird.reset()
        self.pipes.clear()
        self.score = 0
        self.game_over = False

    def create_pipes(self):
        top_pipe, bottom_pipe = PipeFactory.create_pair(
            self.top_pipe_image,
            self.bottom_pipe_image
        )
        self.pipes.append(top_pipe)
        self.pipes.append(bottom_pipe)

    def update(self):
        if self.game_over:
            return

        self.bird.update()

        if self.bird.rect.bottom >= GAME_HEIGHT:
            self.game_over = True
            self.score_manager.save_high_score(self.score)
            return

        for pipe in self.pipes:
            pipe.update()

            if not pipe.passed and self.bird.rect.left > pipe.rect.right:
                self.score += 0.5
                pipe.passed = True

            if self.bird.rect.colliderect(pipe.rect):
                self.game_over = True
                self.score_manager.save_high_score(self.score)
                return

        self.pipes = [pipe for pipe in self.pipes if pipe.rect.right > 0]

        if self.score > self.score_manager.high_score:
            self.score_manager.save_high_score(self.score)

    def draw(self):
        self.window.blit(self.background_image, (0, 0))
        self.bird.draw(self.window)

        for pipe in self.pipes:
            pipe.draw(self.window)

        score_text = f"Score: {int(self.score)}"
        high_score_text = f"Best: {int(self.score_manager.high_score)}"

        score_render = self.font.render(score_text, True, "white")
        high_score_render = self.font.render(high_score_text, True, "white")

        self.window.blit(score_render, (10, 10))
        self.window.blit(high_score_render, (10, 45))

        if self.game_over:
            game_over_render = self.font.render(
                "Game Over - Press SPACE",
                True,
                "white"
            )
            rect = game_over_render.get_rect(
                center=(GAME_WIDTH // 2, GAME_HEIGHT // 2)
            )
            self.window.blit(game_over_render, rect)

        pygame.display.update()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == self.create_pipes_timer and not self.game_over:
                self.create_pipes()

            if event.type == pygame.KEYDOWN:
                if event.key in (pygame.K_SPACE, pygame.K_x, pygame.K_UP):
                    if self.game_over:
                        self.reset()
                    else:
                        self.bird.jump()

    def run(self):
        while True:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(FPS)


if __name__ == "__main__":
    game = Game()
    game.run()