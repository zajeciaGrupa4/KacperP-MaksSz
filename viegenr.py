def szyfruj_vigenere(tekst, klucz):
    wynik = ""
    key_index = 0

    klucz = klucz.upper()

    for litera in tekst:
        if litera.isalpha():
            tekst_val = ord(litera.upper()) - ord('A')

            klucz_litera = klucz[key_index % len(klucz)]
            klucz_val = ord(klucz_litera) - ord('A')

            zaszyfrowana_val = (tekst_val + klucz_val) % 26

            wynik += chr(zaszyfrowana_val + ord('A'))

            key_index += 1
        else:
            wynik += litera

    return wynik


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
            tekst_val = ord(litera.upper()) - ord('A')

            klucz_val = ord(klucz[key_index % len(klucz)]) - ord('A')

            odszyfrowana_val = (tekst_val - klucz_val) % 26

            wynik += chr(odszyfrowana_val + ord('A'))
            key_index += 1
        else:
            wynik += litera

    return wynik