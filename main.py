import pytest

print("Działa!")
import pytest
from viegenr import szyfruj_vigenere, deszyfruj_vigenere
from cezar import szyfr_cezara


@pytest.mark.parametrize("tekst, klucz, oczekiwany", [
    ("AAAA", "CDE", "CDEC"),
    ("ABC", "KOT", "KPV"),
    ("", "KLUCZ", ""),
    ("HELLO", "A", "HELLO"),
    ("XYZ", "B", "YZA"),
    ("123 !@#", "ABC", "123 !@#"),
    ("alamakota", "KOT", "KZTWODYHT"),
    ("Ala Ma Kota", "kot", "KZT WO DYHT"),
])
def test_szyfrowanie_vigenere(tekst, klucz, oczekiwany):
    assert szyfruj_vigenere(tekst, klucz) == oczekiwany

@pytest.mark.parametrize("tekst, klucz, oryginalny", [
    ("KZTWODYHT", "KOT", "ALAMAKOTA"),
    ("CDEC", "CDE", "AAAA"),
    ("YZA", "B", "XYZ"),
])
def test_deszyfruj_vigenere(tekst, klucz, oryginalny):
    assert deszyfruj_vigenere(tekst, klucz) == oryginalny.upper()
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