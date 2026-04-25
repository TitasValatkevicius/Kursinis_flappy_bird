import os
import unittest
import pygame

from flappy_bird import Bird, PipeFactory, ScoreManager
from flappy_bird import BIRD_WIDTH, BIRD_HEIGHT, PIPE_WIDTH, PIPE_HEIGHT


class TestScoreManager(unittest.TestCase):
    def setUp(self):
        self.test_file = "test_highscore.txt"

    def tearDown(self):
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_high_score_starts_at_zero_if_file_missing(self):
        score_manager = ScoreManager(self.test_file)
        self.assertEqual(score_manager.high_score, 0.0)

    def test_high_score_is_saved(self):
        score_manager = ScoreManager(self.test_file)
        score_manager.save_high_score(10)

        new_score_manager = ScoreManager(self.test_file)
        self.assertEqual(new_score_manager.high_score, 10)

    def test_lower_score_does_not_replace_high_score(self):
        score_manager = ScoreManager(self.test_file)
        score_manager.save_high_score(10)
        score_manager.save_high_score(5)

        self.assertEqual(score_manager.high_score, 10)


class TestBird(unittest.TestCase):
    def setUp(self):
        pygame.init()
        self.image = pygame.Surface((BIRD_WIDTH, BIRD_HEIGHT))

    def test_bird_resets_to_start_position(self):
        bird = Bird(self.image)
        bird.rect.y = 100
        bird.velocity_y = 5

        bird.reset()

        self.assertEqual(bird.velocity_y, 0)
        self.assertEqual(bird.rect.y, 320)

    def test_bird_jump_changes_velocity(self):
        bird = Bird(self.image)
        bird.jump()

        self.assertEqual(bird.velocity_y, -6)


class TestPipeFactory(unittest.TestCase):
    def setUp(self):
        pygame.init()
        self.top_image = pygame.Surface((PIPE_WIDTH, PIPE_HEIGHT))
        self.bottom_image = pygame.Surface((PIPE_WIDTH, PIPE_HEIGHT))

    def test_pipe_factory_creates_two_pipes(self):
        top_pipe, bottom_pipe = PipeFactory.create_pair(
            self.top_image,
            self.bottom_image
        )

        self.assertEqual(top_pipe.rect.width, PIPE_WIDTH)
        self.assertEqual(bottom_pipe.rect.width, PIPE_WIDTH)

    def test_bottom_pipe_is_below_top_pipe(self):
        top_pipe, bottom_pipe = PipeFactory.create_pair(
            self.top_image,
            self.bottom_image
        )

        self.assertGreater(bottom_pipe.rect.y, top_pipe.rect.y)


if __name__ == "__main__":
    unittest.main(verbosity=2)