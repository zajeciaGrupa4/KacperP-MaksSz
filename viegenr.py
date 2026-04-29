def szyfruj_vigenere(tekst, klucz):
    wynik = ""
    key_index = 0
    klucz = klucz.upper()

    for litera in tekst:
        if litera.isalpha():
            # Sprawdzamy, czy oryginalna litera była mała czy wielka
            is_lowercase = litera.islower()

            # Obliczenia na wielkich literach dla uproszczenia
            tekst_val = ord(litera.upper()) - ord('A')
            klucz_val = ord(klucz[key_index % len(klucz)]) - ord('A')

            zaszyfrowana_val = (tekst_val + klucz_val) % 26
            nowa_litera = chr(zaszyfrowana_val + ord('A'))

            # Przywracamy małą literę, jeśli taka była na wejściu
            wynik += nowa_litera.lower() if is_lowercase else nowa_litera

            key_index += 1
        else:
            # Znaki specjalne, spacje i cyfry zostają bez zmian
            wynik += litera

    return wynik