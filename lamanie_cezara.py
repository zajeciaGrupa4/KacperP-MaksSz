def lamanie_cezara(zaszyfrowany_tekst):
    """
    Próbuje złamać szyfr Cezara metodą brute-force, analizując częstotliwość
    występowania popularnych polskich liter.
    """
    polskie_litery = ['a', 'e', 'o', 'i', 'n', 's']
    najlepszy_wynik = ""
    max_trafien = -1
    prawdopodobny_klucz = 0

    # Te printy będą widoczne podczas budowania dokumentacji,
    # dopóki nie przeniesiesz logiki wyświetlania poza funkcję.
    print(f"Rozpoczynam łamanie tekstu: {zaszyfrowany_tekst}\n")

    for klucz in range(1, 26):
        probny_tekst = ""
        licznik_popularnych = 0

        for litera in zaszyfrowany_tekst:
            if litera.isalpha():
                kod = ord(litera.lower()) - klucz
                if kod < ord('a'):
                    kod += 26
                nowa_litera = chr(kod)
                probny_tekst += nowa_litera

                if nowa_litera in polskie_litery:
                    licznik_popularnych += 1
            else:
                probny_tekst += litera

        print(f"Klucz {klucz:2}: {probny_tekst}")

        if licznik_popularnych > max_trafien:
            max_trafien = licznik_popularnych
            najlepszy_wynik = probny_tekst
            prawdopodobny_klucz = klucz

    print("-" * 30)
    print(f"Najbardziej prawdopodobny wynik (klucz {prawdopodobny_klucz}):")
    print(f"-> {najlepszy_wynik}")

    return najlepszy_wynik  # Dobra praktyka: funkcja powinna coś zwracać


# SEKCJA TESTOWA:
if __name__ == "__main__":
    # To wykona się tylko przy bezpośrednim uruchomieniu pliku lamanie_cezara.py
    tekst = "dndpdkrwd"  # "alamakota" przesunięte o 3
    lamanie_cezara(tekst)