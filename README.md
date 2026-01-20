# Lista-de-cumparaturi

Aplicația realizată de mine permite gestionarea unei liste de cumpărături direct din linia de comandă. Prin intermediul acesteia, utilizatorul poate adăuga, șterge, lista și căuta produse. De asemenea, are posibilitatea și de a afla totalul sau subtotalul unei anumite categorii, precum și exportarea listei în format CSV. Toate aceste funcționalități pot fi vizualizate prin rularea comenzii help.

## Autor
- **Nume:** Dâlja Sara-Alessandra
- **Grupă:** 2.1
- **Email:** sara-alessandra.dalja@student.upt.ro
- **An academic:** 2025-2026

## Descriere

Această aplicație este o aplicație de tip CLI (Command Line Interface) pentru gestionarea unei liste de cumpărături. Utilizatorul poate adăuga, șterge, lista și căuta articole, fiecare articol având un nume, o cantitate, un preț unitar și o categorie.

Aplicația este utilă pentru organizarea cumpărăturilor zilnice și pentru calcularea rapidă a costurilor totale și a subtotalurilor pe categorii. Datele sunt salvate local într-un fișier JSON, ceea ce permite păstrarea informațiilor între rulări fără a fi necesară utilizarea unei baze de date.

Prin folosirea comenzilor din linia de comandă, aplicația oferă o soluție simplă și rapidă pentru gestionarea listelor de cumpărături, fiind ușor  de extins cu funcționalități noi.

## Tehnologii folosite
- **Limbaj:** Python 3.10
- **Biblioteci:**
  - json - pentru citirea și scrierea datelor în fișier JSON
  - csv - pentru exportul listei de cumpărături în format CSV
- **Tools:** Git,  Docker, Docker Hub

## Cerințe sistem
- **Compilator/Interpretor:** Python 3.10
- **Sistem de operare:** orice sistem care suportă Docker (Windows, Linux, macOS)
- **Dependențe externe:** Docker, Docker Hub

## Instalare

```bash
# Descărcare imagine publică
docker pull saraqwiix/lista-de-cumparaturi

# Clone repository 
git clone https://github.com/saraqwiix/Lista-de-cumparaturi
cd lista-de-cumparaturi
```

## Instalare dependențe

Dacă vreți să rulați aplicația local, fără Docker, instalează dependențele Python necesare:

```bash
# Crearea unui mediu virtual
python3 -m venv venv
source venv/bin/accurate  # Linux / macOS
venv\Scripts\activate     # Windows

# Instalează bibliotecile necesare
pip install --upgrade pip
# json și csv sunt biblioteci standard Python, deci nu e nevoie să fie instalate
```

## Build
Proiectul poate fi rulat direct din Docker, fără a fi nevoie să compilați codul.

### Exemple de comenzi

```bash
docker run saraqwiix/lista-de-cumparaturi add "exemplu"
docker run saraqwiix/lista-de-cumparaturi list
```

### Exemple de utilizare

Exemplul 1: Adăugare articol
```bash
$ docker run saraqwiix/lista-de-cumparaturi add "mere" 5 2.5 "fructe"
```

Output așteptat:
```bash
Articol adăugat cu succes: mere (cantitate: 5, pret: 2.5, total: 12.5, categorie: fructe)
```

Exemplul 2: Listare articole
```bash
$ docker run saraqwiix/lista-de-cumparaturi list
```

Output așteptat:
```bash
Lista de cumpărături:
- mere | cantitate: 5 | pret: 2.5 | total: 12.5 | categorie: fructe
```

Exemplul 3: Ștergere articol

```bash
$ docker run saraqwiix/lista-de-cumparaturi remove "mere"
```

Output așteptat:

```bash
Articolul 'mere' a fost sters cu succes
```

Exemplul 4: Cost total
```bash
$ docker run saraqwiix/lista-de-cumparaturi total
```

Output așteptat:
```bash
Cost total: 12.5 RON
Articole: 1
```

Exemplul 5: Export CSV
```bash
$ docker run saraqwiix/lista-de-cumparaturi export lista.csv
```

Output așteptat:
```bash
Lista a fost exportata cu succes in lista.csv
```

Funcționalități implementate
- [x] Adăugare articole cu nume, cantitate, preț și categorie
- [x] Ștergere articole după nume
- [x] Listare articole cu opțiuni de sortare
- [x] Căutare și filtrare după categorie
- [x] Calcul cost total și subtotaluri pe categorii
- [x] Export listă în format CSV
- [x] Validare date de intrare (cantități zero, prețuri negative)

## Structura proiectului

```bash
lista-de-cumparaturi/
├── Dockerfile – configurarea imaginii Docker
├── README.md – documentația proiectului
├── lista_de_cumparaturi.json – fișier pentru persistența datelor
├── lista.csv – fișier CSV generat la export
├── app/
│ └── main.py – aplicația CLI principală
└── python3 – interpreter utilizat în container
```

## Decizie de design

Am ales să stochez articolele din lista de cumpărături într-o listă de dicționare Python, salvată într-un fișier JSON, deoarece această structură este mai ușor de înțeles și de extins, dar și ușor de salvat și încărcat fără a fi nevoie de o bază de date.

Aplicația este controlată prin comenzi din linia de comandă (add, remove, list, total, search, export), folosind sys.argv, deoarece este ușor de testat și automatizat. De asemenea, se pot adăuga ușor comenzi noi fără a schimba structura aplicației, acest detaliu a fost foarte important de la început ca să pot schimba ușor funcțiile între ele fără să afecteze tot codul.

### Cum ați rezolvat o problemă complexă?

## Probleme întâlnite și soluții

### Problemă: Introducerea unor valori invalide pentru cantitate sau preț
Soluție: Am implementat validări care împiedică salvarea articolelor cu cantitate zero sau preț negativ

### Problemă: În timpul dezvoltării aplicației, au apărut erori de tip IndentationError, cauzate de folosirea amestecată a tab-urilor și spațiilor în cod.

Soluție: Am standardizat indentarea folosind doar spații (4 spații per nivel), conform convenției Python, și am verificat structura funcțiilor pentru a mă asigura că fiecare bloc este corect încadrat. După uniformizarea indentării, erorile au dispărut.

## Testare

### Cum să rulați testele

Aplicația nu folosește teste automate. Testarea a fost realizată manual prin rularea comenzilor din linia de comandă.

Comenzi de test utilizate:

```bash
$ docker run saraqwiix/lista-de-cumparaturi help
$ docker run saraqwiix/lista-de-cumparaturi add "mere" 5 2.5 "fructe"
$ docker run saraqwiix/lista-de-cumparaturi list
$ docker run saraqwiix/lista-de-cumparaturi search --category "fructe"
$ docker run saraqwiix/lista-de-cumparaturi total
$ docker run saraqwiix/lista-de-cumparaturi export lista.csv
```

## Docker

### Build imagine

```bash
docker build -t lista-de-cumparaturi .
```

### Rulare container

```bash
docker pull saraqwiix/lista-de-cumparaturi
docker run saraqwiix/lista-de-cumparaturi help
```

## Resurse folosite

Python – Documentație oficială
https://docs.python.org/3/

Modulul json – Python Standard Library
https://docs.python.org/3/library/json.html

Modulul csv – Python Standard Library
https://docs.python.org/3/library/csv.html

Docker – Documentație oficială
https://docs.docker.com/

Tutorial Docker CLI (referință generală)
https://docs.docker.com/get-started/

## Licență

MIT License

## Contact

Pentru întrebări: sara-alessandra.dalja@student.upt.ro# Lista-de-cumparaturi

Aplicația realizată de mine permite gestionarea unei liste de cumpărături direct din linia de comandă. Prin intermediul acesteia, utilizatorul poate adăuga, șterge, lista și căuta produse. De asemenea, are posibilitatea și de a afla totalul sau subtotalul unei anumite categorii, precum și exportarea listei în format CSV. Toate aceste funcționalități pot fi vizualizate prin rularea comenzii help.

## Autor
- **Nume:** Dâlja Sara-Alessandra
- **Grupă:** 2.1
- **Email:** sara-alessandra.dalja@student.upt.ro
- **An academic:** 2025-2026

## Descriere

Această aplicație este o aplicație de tip CLI (Command Line Interface) pentru gestionarea unei liste de cumpărături. Utilizatorul poate adăuga, șterge, lista și căuta articole, fiecare articol având un nume, o cantitate, un preț unitar și o categorie.

Aplicația este utilă pentru organizarea cumpărăturilor zilnice și pentru calcularea rapidă a costurilor totale și a subtotalurilor pe categorii. Datele sunt salvate local într-un fișier JSON, ceea ce permite păstrarea informațiilor între rulări fără a fi necesară utilizarea unei baze de date.

Prin folosirea comenzilor din linia de comandă, aplicația oferă o soluție simplă și rapidă pentru gestionarea listelor de cumpărături, fiind ușor  de extins cu funcționalități noi.

## Tehnologii folosite
- **Limbaj:** Python 3.10
- **Biblioteci:**
  - json - pentru citirea și scrierea datelor în fișier JSON
  - csv - pentru exportul listei de cumpărături în format CSV
- **Tools:** Git,  Docker, Docker Hub

## Cerințe sistem
- **Compilator/Interpretor:** Python 3.10
- **Sistem de operare:** orice sistem care suportă Docker (Windows, Linux, macOS)
- **Dependențe externe:** Docker, Docker Hub

## Instalare

```bash
# Descărcare imagine publică
docker pull saraqwiix/lista-de-cumparaturi

# Clone repository 
git clone https://github.com/saraqwiix/Lista-de-cumparaturi
cd lista-de-cumparaturi
```

## Instalare dependențe

Dacă vreți să rulați aplicația local, fără Docker, instalează dependențele Python necesare:

```bash
# Crearea unui mediu virtual
python3 -m venv venv
source venv/bin/accurate  # Linux / macOS
venv\Scripts\activate     # Windows

# Instalează bibliotecile necesare
pip install --upgrade pip
# json și csv sunt biblioteci standard Python, deci nu e nevoie să fie instalate
```

## Build
Proiectul poate fi rulat direct din Docker, fără a fi nevoie să compilați codul.

### Exemple de comenzi

```bash
docker run saraqwiix/lista-de-cumparaturi add "exemplu"
docker run saraqwiix/lista-de-cumparaturi list
```

### Exemple de utilizare

Exemplul 1: Adăugare articol
```bash
$ docker run saraqwiix/lista-de-cumparaturi add "mere" 5 2.5 "fructe"
```

Output așteptat:
```bash
Articol adăugat cu succes: mere (cantitate: 5, pret: 2.5, total: 12.5, categorie: fructe)
```

Exemplul 2: Listare articole
```bash
$ docker run saraqwiix/lista-de-cumparaturi list
```

Output așteptat:
```bash
Lista de cumpărături:
- mere | cantitate: 5 | pret: 2.5 | total: 12.5 | categorie: fructe
```

Exemplul 3: Ștergere articol

```bash
$ docker run saraqwiix/lista-de-cumparaturi remove "mere"
```

Output așteptat:

```bash
Articolul 'mere' a fost sters cu succes
```

Exemplul 4: Cost total
```bash
$ docker run saraqwiix/lista-de-cumparaturi total
```

Output așteptat:
```bash
Cost total: 12.5 RON
Articole: 1
```

Exemplul 5: Export CSV
```bash
$ docker run saraqwiix/lista-de-cumparaturi export lista.csv
```

Output așteptat:
```bash
Lista a fost exportata cu succes in lista.csv
```

Funcționalități implementate
- [x] Adăugare articole cu nume, cantitate, preț și categorie
- [x] Ștergere articole după nume
- [x] Listare articole cu opțiuni de sortare
- [x] Căutare și filtrare după categorie
- [x] Calcul cost total și subtotaluri pe categorii
- [x] Export listă în format CSV
- [x] Validare date de intrare (cantități zero, prețuri negative)

## Structura proiectului

```bash
lista-de-cumparaturi/
├── Dockerfile – configurarea imaginii Docker
├── README.md – documentația proiectului
├── lista_de_cumparaturi.json – fișier pentru persistența datelor
├── lista.csv – fișier CSV generat la export
├── app/
│ └── main.py – aplicația CLI principală
└── python3 – interpreter utilizat în container
```

## Decizie de design

Am ales să stochez articolele din lista de cumpărături într-o listă de dicționare Python, salvată într-un fișier JSON, deoarece această structură este mai ușor de înțeles și de extins, dar și ușor de salvat și încărcat fără a fi nevoie de o bază de date.

Aplicația este controlată prin comenzi din linia de comandă (add, remove, list, total, search, export), folosind sys.argv, deoarece este ușor de testat și automatizat. De asemenea, se pot adăuga ușor comenzi noi fără a schimba structura aplicației, acest detaliu a fost foarte important de la început ca să pot schimba ușor funcțiile între ele fără să afecteze tot codul.

### Cum ați rezolvat o problemă complexă?

## Probleme întâlnite și soluții

Problemă: Introducerea unor valori invalide pentru cantitate sau preț
Soluție: Am implementat validări care împiedică salvarea articolelor cu cantitate zero sau preț negativ

Problemă:
În timpul dezvoltării aplicației, au apărut erori de tip IndentationError, cauzate de folosirea amestecată a tab-urilor și spațiilor în cod.

Soluție:
Am standardizat indentarea folosind doar spații (4 spații per nivel), conform convenției Python, și am verificat structura funcțiilor pentru a mă asigura că fiecare bloc este corect încadrat. După uniformizarea indentării, erorile au dispărut.

## Testare

### Cum să rulați testele

Aplicația nu folosește teste automate. Testarea a fost realizată manual prin rularea comenzilor din linia de comandă.

Comenzi de test utilizate:

```bash
$ docker run saraqwiix/lista-de-cumparaturi help
$ docker run saraqwiix/lista-de-cumparaturi add "mere" 5 2.5 "fructe"
$ docker run saraqwiix/lista-de-cumparaturi list
$ docker run saraqwiix/lista-de-cumparaturi search --category "fructe"
$ docker run saraqwiix/lista-de-cumparaturi total
$ docker run saraqwiix/lista-de-cumparaturi export lista.csv
```

## Docker

### Build imagine

```bash
docker build -t lista-de-cumparaturi .
```

### Rulare container

```bash
docker pull saraqwiix/lista-de-cumparaturi
docker run saraqwiix/lista-de-cumparaturi help
```

## Resurse folosite

Python – Documentație oficială
https://docs.python.org/3/

Modulul json – Python Standard Library
https://docs.python.org/3/library/json.html

Modulul csv – Python Standard Library
https://docs.python.org/3/library/csv.html

Docker – Documentație oficială
https://docs.docker.com/

Tutorial Docker CLI (referință generală)
https://docs.docker.com/get-started/

## Licență

MIT License

## Contact

Pentru întrebări: sara-alessandra.dalja@student.upt.ro

