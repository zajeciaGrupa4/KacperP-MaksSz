def szyfr_cezara(tekst, klucz):
    wynik = ""
    for litera in tekst:
        if litera.isalpha() and 'a' <= litera.lower() <= 'z':
            litera = ord(litera.lower()) + klucz
        if litera > ord('z'):
            litera -= 26
        elif litera < ord('a'):
            litera += 26
        wynik += chr(litera)
    return wynik
n = "alamakota"
k = 3
print(szyfr_cezara(n, k))