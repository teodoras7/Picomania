# Picomania

Picomania este o platformă interactivă care conține 4 jocuri, fiecare dintre ele fiind implementat cu muzică și culori, iar 3 dintre ele având câte 2 variante de a fi jucate. Platforma conține un meniu complex care permite jucătorului să aleagă și să realeagă jocul dorit. Mai multe detalii sunt în secțiunea: **"Conectarea jocurilor"**.

## Elemente utilizate:

* Raspberry Pi Pico;
* un potențiometru;
* 3 fire, 2 folosite la potențiometru și unul la Audio;
* cabluri de conectare la laptop + laptop (cu VSCode și Python).

## Jocurile:

Cele 4 jocuri se numesc:

1. **Simon Says**
2. **Be Fast**
3. **Catch Apples**
4. **Blackjack**

---

## 1) Simon Says

### Descriere:

Scopul jocului este ca jucătorul să memoreze combinațiile și apoi să demonstreze că le-a reținut bine.

### Variante:

#### 5 Niveluri:

Dacă jucătorul trece de cele 5 niveluri, apare mesajul de **CONGRATULATIONS!** iar dacă pierde pe parcurs, apare **GAME OVER**.

#### Variante Infinită:

Jucătorului i se arată la final un scor reprezentând ultimul nivel terminat.

---

## 2) Be Fast

### Descriere:

Scopul jocului este ca jucătorul să apese cât de repede poate pe pătrățelele care apar. Cu cât scorul crește mai mare, cu atât dificultatea jocului se mărește.

### Variante:

#### Single Player:

Jucătorului i se arată la final un scor reprezentând ultimul nivel terminat.

#### Variante 1v1:

Un jucător joacă pe partea dreaptă, celălalt pe partea stângă, culoarea este doar albă pentru a nu exista derutări.

---

## 3) Catch Apples

### Descriere:

Scopul acestui joc este ca jucătorul să prindă cât mai multe mere în coș. Dificultatea jocului crește cu cât scorul se mărește. Jucătorului i se arată la final un scor reprezentând ultimul nivel terminat.

### Variante:

#### Butoanele B și Y:

Jucătorul folosește butoanele B și Y pentru a muta coșul.

#### Potențiometru:

Jucătorul folosește potențiometrul pentru a muta coșul. La începutul jocului, potențiometrul trebuie setat cât mai la stânga pentru a avea coșul în colțul corect.

---

## 4) Blackjack

### Descriere:

Acest joc conține regulile obișnuite ale cunoscutului joc **Blackjack**. Jucătorul concurează cu un "Dealer" care își alege random mâna de joc.

---

## Conectarea jocurilor

Pe lângă acest meniu complex, după terminarea fiecărui joc și afișarea rezultatului, jucătorul are la dispoziție 10 secunde să aleagă dacă mai vrea să se joace încă o dată același joc (ajunge în meniul jocului sau începe jocul direct în cazul „Blackjack”) sau dacă vrea alt joc (ajunge în meniul principal). După cele 10 secunde, codul se oprește din rulare și rămâne pe fundal scorul ultimului joc jucat.

---

## Rularea codului

Pentru a juca, trebuie să rulezi fișierul **`jocuri.py`**. Acesta conține logica principală a jocurilor. În plus, pentru a asigura funcționarea completă a platformei, se vor utiliza și următoarele fișiere de referință:

* **`jocuri.py`**: Contine logica jocurilor și meniu;
* **`be_fast.py`**: Codul pentru jocul **Be Fast**;
* **`be_fast_1v1.py`**: Codul pentru varianta 1v1 a jocului **Be Fast**;
* **`black_display.py`**: Fișierul care golește ecranul în cazul în care a rămas ceva pe el de dinainte;
* **`black_jack.py`**: Codul pentru jocul **Blackjack**;
* **`catch_apples.py`**: Codul pentru varianta cu butoanele B si Y a jocului **Catch Apples**;
* **`catch_apples2.py`**: Codul pentru varianta cu potențiometru a jocului **Catch Apples**;
* **`simon_says.py`**: Codul pentru varianta cu 5 niveluri a jocului **Simon Says**;
* **`simon_says_loop.py`**: Codul pentru varianta infinită a jocului **Simon Says**.

### Cum să rulezi proiectul

1. Asigură-te că ai toate fișierele într-un singur director.
2. Deschide terminalul în directorul proiectului.
3. Rulează fișierul principal cu comanda:

```bash
python jocuri.py
```
### Cum să golești ecranul

1. Rulează fișierul specific cu comanda:

```bash
python black_display.py
```
Asigură-te că ai configurat corect Raspberry Pi Pico și conexiunile hardware necesare.

---


