# Dokumentacja: Szyfr Vigenère'a

Szyfr Vigenère'a to klasyczny szyfr polialfabetyczny, który stanowi rozwinięcie szyfru Cezara. Zamiast przesuwać wszystkie litery o tę samą stałą wartość, każda litera tekstu jawnego jest przesuwana o wartość wynikającą z odpowiadającej jej litery słowa-klucza.

## Zasada działania

Szyfr wykorzystuje tzw. Tabulę Recta (tablicę Vigenère'a). Każdą literę tekstu jawnego przesuwa się w alfabecie o tyle pozycji, ile wynosi wartość numeryczna odpowiadającej jej litery w kluczu (gdzie A=0, B=1, ..., Z=25).

[Image of Vigenere square]

### Implementacja w kodzie (`viegenr.py`)

Funkcja `szyfruj_vigenere(tekst, klucz)` realizuje algorytm w następujący sposób:

1. **Przygotowanie klucza**: Klucz jest zamieniany na wielkie litery, aby uniknąć błędów w obliczeniach ASCII.
2. **Iteracja**: Program przechodzi znak po znaku przez tekst wejściowy.
3. **Obsługa liter**:
   - Wyliczany jest indeks litery w alfabecie (0-25).
   - Wyliczany jest indeks przesunięcia z aktualnej litery klucza.
   - Nowa litera powstaje według wzoru: `(tekst_val + klucz_val) % 26`.
   - Program rozpoznaje wielkość liter – jeśli oryginał był mały, wynik również będzie mały.
4. **Znaki specjalne**: Spacje, cyfry i znaki interpunkcyjne są ignorowane przez algorytm szyfrujący (zostają przepisane bez zmian), a licznik klucza w tym czasie "stoi w miejscu".

## Przykładowe szyfrowanie

**Tekst:** `ALA MA KOTA`  
**Klucz:** `KOT`

* **A** + **K** → **K**
* **L** + **O** → **Z**
* **A** + **T** → **T**
* (spacja pozostaje bez zmian)
* **M** + **K** → **W**
* ... i tak dalej.

**Wynik:** `KZT WO DYHT`

## Deszyfrowanie (`lamanie_viegenera.py`)

Proces deszyfrowania jest odwrotnością szyfrowania. Zamiast dodawać wartość klucza, odejmujemy ją od wartości litery zaszyfrowanej:
`oryginal_val = (zaszyfrowany_val - klucz_val) % 26`.

## Zalety i Wady
* **Zaleta**: Odporność na prostą analizę częstotliwościową (ta sama litera 'A' w tekście może stać się różnymi literami w szyfrze).
* **Wada**: Przy krótkim kluczu i długim tekście, wzorce zaczynają się powtarzać, co pozwala na złamanie szyfru metodami statystycznymi.

---
*Plik wygenerowany automatycznie na potrzeby dokumentacji projektu.*