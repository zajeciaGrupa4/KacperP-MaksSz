def szyfruj_vigenere(tekst, klucz):
    wynik = ""
    key_index = 0
    klucz = klucz.upper()

    for litera in tekst:
        if litera.isalpha():
            is_lowercase = litera.islower()

            tekst_val = ord(litera.upper()) - ord('A')
            klucz_val = ord(klucz[key_index % len(klucz)]) - ord('A')

            zaszyfrowana_val = (tekst_val + klucz_val) % 26
            nowa_litera = chr(zaszyfrowana_val + ord('A'))

            wynik += nowa_litera.lower() if is_lowercase else nowa_litera

            key_index += 1
        else:
            wynik += litera

    return wynik