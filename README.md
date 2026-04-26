# Kursinis: Flappy bird
Titas Valatkevičius objektinio programavimo kursinis darbas:

Ši programa yra žaidimas „Flappy Bird“, sukurtas naudojant Python programavimo kalbą ir „pygame“ biblioteką. Žaidimo tikslas yra valdyti paukštį ir išvengiant kliūčių (vamzdžių) rinkti taškus.
Programa sukurta taikant objektinio programavimo (OOP) principus, tokius kaip paveldėjimas, enkapsuliacija, abstrakcija ir polimorfizmas.


## Kaip paleisti flappy_bird programą:
1) Parsisiųsti zip failą.
2) Parsisiųsti pygame: https://www.pygame.org/download.shtml
3) Parsisiųsti python: https://www.python.org/downloads/
4) Atsidaryti zip failą vs code arba kitose programose.
5) Atsidaryti flappy_bird.py.
6) Spausti run python file.

## flappy_bird kontrolės:

Šokti - SPACE, rodyklė į viršų.

Pralaimėjus galima pradėti iš naujo paspaudus - SPACE, rodyklę į viršų.

## Kaip paleisti test_flappy_bird programą:
1) Parsisiųsti zip failą.
2) Atsidaryti zip failą vs code arba kitose programose.
3) Atsidaryti test_flappy_bird.py.
4) Spausti run python file.



## Programa įgyvendina visus pagrindinius reikalavimus ir objektinio programavimo principus:

### 1) Paveldėjimas (Inheritance):
   
  Klasės `Bird` ir `Pipe` paveldi iš bendros klasės `GameObject`:
<img width="455" height="288" alt="image" src="https://github.com/user-attachments/assets/974b4cb2-0258-4764-b5b5-be297d9e7109" />
<img width="1356" height="410" alt="image" src="https://github.com/user-attachments/assets/9d70456c-f7fe-45b5-abfa-55ff80066956" />

### 2) Enkapsuliacija (Encapsulation):
   
   Klasės saugo savo duomenis ir logiką viduje:
<img width="1542" height="938" alt="image" src="https://github.com/user-attachments/assets/cee79c0e-74af-4c63-93c4-485d9c4136cb" />

### 3) Abstrakcija (Abstraction):
   
   `GameObject` klasė apibrėžia bendrą funkcionalumą, objektų piešimą ekrane:
<img width="581" height="204" alt="image" src="https://github.com/user-attachments/assets/5d1db34b-9ea7-4c5c-bac1-e7b97bc5df00" />
   
### 4) Polimorfizmas (Polymorphism):
   
   Skirtingi objektai (`Bird` ir `Pipe`), nors yra skirtingų tipų, gali naudoti tą patį metodą `draw()`, nes paveldi bendrą funkcionalumą iš `GameObject` klasės.
<img width="621" height="163" alt="image" src="https://github.com/user-attachments/assets/8c9d55d7-4cf2-4fb9-9a5b-b18240859f01" />

## Dizaino šablonas (Design Pattern):

Naudojamas Factory Method šablonas per PipeFactory klasę:

<img width="694" height="397" alt="image" src="https://github.com/user-attachments/assets/273cb24d-24e0-4ff9-9a9e-734482a9f159" />

Ši klasė atsakinga už vamzdžių poros sukūrimą su atsitiktine pozicija. Tai leidžia atskirti objektų kūrimo logiką nuo pagrindinės žaidimo logikos.

## Kompozicija / agregacija:

`Game` klasė naudoja kitus objektus (`Bird`, `Pipe`, `ScoreManager`):

<img width="990" height="490" alt="image" src="https://github.com/user-attachments/assets/eeeb0854-ba34-41fb-85ac-fd106340af1a" />

Tai parodo „has-a“ ryšį tarp objektų.

## Failų skaitymas / rašymas:

Naudojama `ScoreManager` klasė, kuri:

1) Nuskaito aukščiausią rezultatą iš failo.
2) Išsaugo naują rekordą į failą.
<img width="723" height="443" alt="image" src="https://github.com/user-attachments/assets/4650707c-064a-493d-a51b-68b8878a113c" />

## Testavimas:

Programa turi unit testus (test_flappy_bird.py), kurie tikrina:

1) Aukščiausio rezultato išsaugojimą.
2) Paukščio veikimą.
3) Vamzdžių kūrimą.

Testai sukurti naudojant unittest biblioteką.

## Rezultatai:

1) Programa sėkmingai veikia ir įgyvendina visus funkcinius reikalavimus.
2) Panaudoti visi 4 OOP principai.
3) Įgyvendintas dizaino šablonas (Factory Method).
4) Sukurti unit testai, kurie tikrina pagrindinį kodo funkcionalumą.

## Išvados:

Šio darbo metu buvo sukurtas pilnai veikiantis „Flappy Bird“ žaidimas, naudojant Python programavimo kalbą ir „pygame“ biblioteką. Projektas sėkmingai įgyvendina visus pagrindinius funkcinius reikalavimus, įskaitant vartotojo valdymą, objektų judėjimą, susidūrimų aptikimą ir taškų skaičiavimą. Darbo metu buvo pritaikyti paveldėjimo, enkapsuliacijos, abstrakcijos ir polimorfizmo principai. Tai leido sukurti struktūruotą, lengvai suprantamą ir išplečiamą programą. Taip pat buvo panaudotas „Factory Method“ dizainas, kuris supaprastina objektų kūrimą. Programa naudoja failų skaitymą ir rašymą, aukščiausio rezultato saugojimui, kas leidžia išlaikyti žaidėjo progresą tarp skirtingų programos paleidimų. Be to, buvo sukurti unit testai, kurie užtikrina pagrindinių funkcijų veikimą ir padeda aptikti galimas kodo klaidas.

## Ateityje programą būtų galima išplėsti:

1) Pridėti garso efektus.
2) Pridėti meniu sistemą.
3) Išsaugoti daugiau statistikos.
4) Pridėti skirtingus sudėtingumo lygius.
5) Sukurti grafiškai patobulintą versiją.
6) Pridėti daugiau paukščio spalvų.
