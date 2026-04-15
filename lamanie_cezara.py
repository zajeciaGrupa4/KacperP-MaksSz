def lamanie_cezara(zaszyfrowany_tekst):
    polskie_litery = ['a', 'e', 'o', 'i', 'n', 's']  # Najczęstsze litery
    najlepszy_wynik = ""
    max_trafien = -1
    prawdopodobny_klucz = 0

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

                # Analiza częstotliwości
                if nowa_litera in polskie_litery:
                    licznik_popularnych += 1
            else:
                probny_tekst += litera

        print(f"Klucz {klucz:2}: {probny_tekst}")

        # Zapamiętujemy wynik z największą liczbą popularnych liter
        if licznik_popularnych > max_trafien:
            max_trafien = licznik_popularnych
            najlepszy_wynik = probny_tekst
            prawdopodobny_klucz = klucz

    print("-" * 30)
    print(f"Najbardziej prawdopodobny wynik (klucz {prawdopodobny_klucz}):")
    print(f"-> {najlepszy_wynik}")


# Testowanie:
tekst = "dndpdkrwd"  # "alamakota" przesunięte o 3
lamanie_cezara(tekst)