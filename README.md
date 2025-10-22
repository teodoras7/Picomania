

# Picomania

Picomania este o platformă interactivă care conține 4 jocuri, fiecare dintre ele fiind implementat cu muzică și culori, iar 3 dintre ele având câte 2 variante de a fi jucate.
Platforma conține un meniu complex care permite jucătorului să aleagă și să realeagă jocul dorit. Mai multe detalii sunt în secțiunea: **"Conectarea jocurilor"**.

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
Jucătorul folosește butoanele B si Y pentru a muta coșul.

#### Potențiometru:

Jucătorul folosește potențiometrul pentru a muta coșul. La început de joc, potențiometrul trebuie setat cât mai la stânga pentru a avea coșul în colțul corect.

---

## 4) Blackjack

### Descriere:

Acest joc conține regulile obișnuite ale cunoscutului joc **Blackjack**. Jucătorul concurează cu un "Dealer" care își alege random mâna de joc.

---

## Conectarea jocurilor

Pe lângă acest meniu complex, după terminarea fiecărui joc și afișarea rezultatului, jucătorul are la dispoziție 10 secunde să aleagă dacă mai vrea să se joace încă o dată același joc (ajunge în al doilea meniu sau începe jocul direct în cazul „Blackjack”) sau dacă vrea alt joc și ajunge în meniul principal. După cele 10 secunde, codul se oprește din rulare și rămâne pe fundal scorul ultimului joc jucat.

---
