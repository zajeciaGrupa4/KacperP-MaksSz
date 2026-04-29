# Dokumentacja szyfru Cezara
## Szyfr Cezara to szyfr podstawiniowy, które polega na zamianie/ podstawieniu za daną literę w tekści jej oddaleniu o podany wcześniej klucz
### Szyfrowanie
- funkcja pobiera tekst składający sie z liter oraz będący l. naturalną klucz
```python
def szyfr_cezara(tekst, klucz):
    wynik = ""
```
- funkcja sprawdza po kolei cały tekst czy są tam tylko litery
```python
 for litera in tekst:
        if litera.isalpha():
```
- funkcja analizuje poszczególne znaki, patrzy na tabele kodów ASCII i przyporządkowuje im odpowiednie litery, sprawdza miejsce, przewiduje małe i duże litery oraz co gdy klucz wychodzi poza alfabet- nadmiar liczy od "a"
```python

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
```
- funkcja zwraca tekst który jest zaszyfrowanym o klucz k tekstem wejściowym
```python
print(szyfr_cezara(n, k))
```