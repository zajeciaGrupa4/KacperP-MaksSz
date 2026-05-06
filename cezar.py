def szyfr_cezara(tekst, klucz):
    """
        Szyfruje tekst przy użyciu klasycznego algorytmu szyfru Cezara.

        Funkcja przesuwa każdą literę w tekście o określoną liczbę miejsc w alfabecie.
        Zachowuje wielkość liter (małe pozostają małe, wielkie pozostają wielkie)
        oraz pomija znaki niebędące literami (np. spacje, cyfry, znaki interpunkcyjne).

        Args:
            tekst (str): Ciąg znaków do zaszyfrowania.
            klucz (int): Liczba miejsc, o które ma nastąpić przesunięcie
                (dodatnia dla szyfrowania w prawo, ujemna dla odszyfrowywania).

        Returns:
            str: Zaszyfrowany tekst wynikowy.
    """
    wynik = " "
    for litera in tekst:
        if litera.isalpha():
            if litera.islower():
                if 'a' <= litera.lower() <= 'z':
                    litera = ord(litera.lower()) + klucz

                if litera > ord('z'):
                    litera -= 26
                elif litera < ord('a'):
                    litera += 26
            elif litera.isupper():
                if 'A' <= litera.upper() <= 'Z':
                    litera = ord(litera.upper()) + klucz

                if litera > ord('Z'):
                    litera -= 26
                elif litera < ord('A'):
                    litera += 26
            wynik += chr(litera)
        else:
            wynik += litera
    return wynik
n = "Hello, World!"
k = 3
if __name__ == "__main__":
    print(szyfr_cezara("Hello World", 3))