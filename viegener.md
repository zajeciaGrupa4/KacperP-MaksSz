# Dokumentacja Techniczna: Implementacja Szyfru Vigenère'a

Dokument ten opisuje strukturę i logikę dwóch kluczowych modułów projektu: `viegenr.py` (szyfrowanie) oraz `lamanie_viegenera.py` (deszyfrowanie).

---

## 1. Architektura kodu
Projekt opiera się na modułowości, co pozwala na niezależne zarządzanie procesem kodowania i dekodowania danych.

### Główne komponenty:
* **Logika matematyczna**: Wykorzystanie arytmetyki modulo do operacji na alfabecie.
* **Zarządzanie kluczem**: Dynamiczne dopasowanie długości hasła do długości tekstu.
* **Walidacja danych**: Rozróżnianie znaków alfabetycznych od znaków specjalnych.

---

## 2. Analiza funkcji szyfrującej (`viegenr.py`)
Funkcja `szyfruj_vigenere` odpowiada za zamianę tekstu jawnego na szyfrogram.

### Kluczowe operacje:
1.  **Normalizacja klucza**:
    - `klucz.upper()` – ujednolicenie wielkości liter hasła dla stałych wartości przesunięć.
2.  **Szyfrowanie właściwe**:
    - `zaszyfrowana_val = (tekst_val + klucz_val) % 26`
    - **Opis**: Dodanie wartości litery tekstu i klucza. Wynik modulo 26 gwarantuje pozostanie w zakresie alfabetu A-Z.
3.  **Zachowanie formatowania**:
    - `if litera.isalpha()` – szyfrowanie pomija spacje i znaki specjalne, przepisując je bezpośrednio do wyniku.

---

## 3. Analiza funkcji deszyfrującej (`lamanie_viegenera.py`)
Funkcja `deszyfruj_vigenere` przywraca oryginalną treść wiadomości przy użyciu tego samego klucza.

### Mechanizm działania:
* **Operacja odwrotna**:
    - `odszyfrowana_val = (tekst_val - klucz_val) % 26`
    - **Podpunkt**: Zamiast dodawania, odejmujemy przesunięcie klucza.
* **Normalizacja ASCII**:
    - `chr(odszyfrowana_val + ord('A'))` – powrót z wartości numerycznej na znak tekstowy.

---

## 4. Wspólne mechanizmy sterujące
Oba pliki współdzielą te same zasady zarządzania przepływem danych:

### Zarządzanie indeksem klucza:
- `key_index % len(klucz)`
  - Pozwala na nieskończone powtarzanie krótkiego hasła dla długich tekstów.
  - Indeks zwiększa się **tylko** po napotkaniu litery, co zapobiega przesunięciu klucza na spacjach.

### Obsługa wielkości liter:
- Program zamienia litery na wielkie (`.upper()`) przed obliczeniami, co upraszcza logikę (używamy tylko jednej bazy `ord('A')`).

---

*Dokumentacja przygotowana dla projektu kryptograficznego.*