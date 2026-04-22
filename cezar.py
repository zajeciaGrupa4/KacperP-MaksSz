def szyfr_cezara(tekst, klucz):
    wynik = ""
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
print(szyfr_cezara(n, k))