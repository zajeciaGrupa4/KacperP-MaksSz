# 1. Definicja - widoczna dla Sphinxa i innych plików
def deszyfruj_vigenere(tekst, klucz):
    """
    Odszyfrowuje tekst zaszyfrowany szyfrem Vigenere'a.
    """
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

# 2. Wywołanie - to Sphinx zignoruje, a Ty zobaczysz w konsoli
if __name__ == "__main__":
    testowy_tekst = "KZT WO DYHT"
    testowy_klucz = "KOT"
    print(f"Odszyfrowany tekst: {deszyfruj_vigenere(testowy_tekst, testowy_klucz)}")