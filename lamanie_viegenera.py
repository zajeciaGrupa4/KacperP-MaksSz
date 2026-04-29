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