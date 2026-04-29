# Projekt kryptograficzny 

Program zawiera:
- Szyfr Cezara
  - Szyfr Cezara to prosty szyfr podstawieniowy,  w który każdą literę tekstu zastępuje  sie literą przesuniętą o stałą liczbę pozycji w alfabecie.
- Szyfr Viegenera
  - Szyfr Viegenere'a to szyfr polialfabetyczny, w którym każda litera tekstu jest przesuwana o różną liczbę pozycji zależną od powtarzanego hasła(klucza).
- Program łamiący szyfr Cezara
  - Program działa metodą „siłową” (Brute-force). Przeszukuje on wszystkie 25 możliwych kombinacji przesunięcia alfabetu i wyświetla je jedna po drugiej. Dzięki temu można błyskawicznie odnaleźć czytelną treść bez znajomości klucza.
- Program łamiący szyfr Viegenera
  - Program wykorzystuje analizę statystyczną tekstu. Najpierw próbuje zgadnąć długość hasła, szukając powtarzających się wzorów, a następnie dopasowuje litery klucza na podstawie tego, jak często dane znaki występują w danym języku. Pozwala to odczytać wiadomość nawet przy długim i skomplikowanym haśle.

## Funkcjonalność

---

1. Szyfrowanie i deszyfrowanie tekstu przy użyciu szyfru Cezara
2. Szyfrowanie i deszyfrowanie tekstu przy użyciu szyfru Viegenera
3. Generowanie losowych kluczy
4. Próba łamania zaszyfrowanych wiadomości

## Instalacja

---
Pobieranie repozytorium:
```bash
git clone [https://github.com/zajeciaGrupa4/KacperP-MaksSz.git](https://github.com/zajeciaGrupa4/KacperP-MaksSz.git)
```
## Urucomienie

---
```python main.py```

## Struktura projektu

---

- ```maint.py``` - główny plik programu   
- ```cezar.py``` - implementacja szyfru Cezara
- ```viegenr.py``` - implementacja szyfru Viegenera
- ```lamanie_cezara.py``` - łamanie szyfru
- ```lamanie_viegenera.py``` - łamanie viegenera