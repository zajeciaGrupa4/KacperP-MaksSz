def szyfruj_vigenere(tekst, klucz):
    """
    Szyfruje tekst za pomocą szyfru Vigenère’a.

    :param tekst: tekst do zaszyfrowania
    :param klucz: hasło (klucz) używane do przesuwania liter
    :return: Zaszyfrowany tekst z zachowaniem wielkości liter
    """
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

# --- TO JEST KLUCZOWA CZĘŚĆ ---
if __name__ == "__main__":
    # Wszystko, co jest W TYM BLOKU, Sphinx zignoruje.
    # Wykona się to TYLKO wtedy, gdy klikniesz "Run" w PyCharmie.
    test_tekst = "ALA MA KOTA"
    test_klucz = "KOT"
    print(f"Wynik: {szyfruj_vigenere(test_tekst, test_klucz)}")