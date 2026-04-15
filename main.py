print("Działa!")

from viegenr import szyfruj_vigenere, deszyfruj_vigenere

oryginalny = "ALAMAKOTA"
klucz = "KOT"

zaszyfrowany = szyfruj_vigenere(oryginalny, klucz)
odszyfrowany = deszyfruj_vigenere(zaszyfrowany, klucz)

print(f"Oryginał: {oryginalny}")
print(f"Szyfr:    {zaszyfrowany}")
print(f"Powrót:   {odszyfrowany}")

if oryginalny == odszyfrowany:
    print("\n✅ Wszystko działa poprawnie!")