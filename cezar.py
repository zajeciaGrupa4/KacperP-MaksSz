def szyfr_cezara(tekst, klucz):
    wynik = ""
    for litera in tekst:
        kod = ord(litera) + klucz
        wynik += chr(kod)
    return wynik
n = "alamakota"
k = 3
print(szyfr_cezara(n, k))