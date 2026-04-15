def szyfruj_vigenere(tekst, klucz):
    wynik = ""
    key_index = 0

    # Upewniamy się, że klucz jest wielkimi literami dla ułatwienia obliczeń
    klucz = klucz.upper()

    for litera in tekst:
        if litera.isalpha():  # Szyfrujemy tylko litery
            # 1. Uzyskujemy wartość liczbową litery tekstu (0-25)
            tekst_val = ord(litera.upper()) - ord('A')

            # 2. Uzyskujemy wartość przesunięcia z klucza (0-25)
            # Używamy modulo (%), aby klucz "zawijał się", gdy jest krótszy niż tekst
            klucz_litera = klucz[key_index % len(klucz)]
            klucz_val = ord(klucz_litera) - ord('A')

            # 3. Dodajemy wartości i stosujemy modulo 26 (rozmiar alfabetu)
            zaszyfrowana_val = (tekst_val + klucz_val) % 26

            # 4. Zamieniamy z powrotem na literę
            wynik += chr(zaszyfrowana_val + ord('A'))

            # Przesuwamy indeks klucza tylko, gdy przetworzyliśmy literę
            key_index += 1
        else:
            # Jeśli to spacja lub znak specjalny, dodajemy bez zmian
            wynik += litera

    return wynik


# Przykład użycia:
wiadomosc = "ALAMAKOTA"
haslo = "KOT"
print(f"Tekst: {wiadomosc}")
print(f"Klucz: {haslo}")
print(f"Wynik: {szyfruj_vigenere(wiadomosc, haslo)}")


def deszyfruj_vigenere(tekst, klucz):
    wynik = ""
    key_index = 0
    klucz = klucz.upper()

    for litera in tekst:
        if litera.isalpha():
            # 1. Wartość litery zaszyfrowanej (0-25)
            tekst_val = ord(litera.upper()) - ord('A')

            # 2. Wartość klucza (0-25)
            klucz_val = ord(klucz[key_index % len(klucz)]) - ord('A')

            # 3. ODEJMOWANIE (odwracamy przesunięcie)
            # Python automatycznie obsłuży ujemne wyniki dzięki modulo, np. -1 % 26 = 25
            odszyfrowana_val = (tekst_val - klucz_val) % 26

            # 4. Powrót do znaku ASCII
            wynik += chr(odszyfrowana_val + ord('A'))
            key_index += 1
        else:
            wynik += litera

    return wynik