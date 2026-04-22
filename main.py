import pytest

print("Działa!")

from viegenr import szyfruj_vigenere, deszyfruj_vigenere
from cezar import szyfr_cezara

oryginalny = "ALAMAKOTA"
klucz = "KOT"

zaszyfrowany = szyfruj_vigenere(oryginalny, klucz)
odszyfrowany = deszyfruj_vigenere(zaszyfrowany, klucz)

print(f"Oryginał: {oryginalny}")
print(f"Szyfr:    {zaszyfrowany}")
print(f"Powrót:   {odszyfrowany}")

@pytest.mark.parametrize("text, key, expected", [
    ("abc", 1, "bcd"),
    ("xyz", 2, "zab"),
    ("hello", 3, "khoor"),
    ("python", 5, "udymts"),
    ("abc", 26, "abc"),
    ("ABC", 1, "BCD"),
    ("Hello, World!", 3, "Khoor, Zruog!"),
    ("test123", 4, "xiwx123"),
    ("zzz", 1, "aaa"),
    ("attackatdawn", 7, "haahjrhakhdu"),
])

def test_ceaser(text, key, expected):
    assert szyfr_cezara(text, key) == expected

if oryginalny == odszyfrowany:
    print("\n✅ Wszystko działa poprawnie!")