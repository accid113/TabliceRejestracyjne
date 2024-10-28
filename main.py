import pytesseract
import cv2
import re

def spr(numer):
    wzor = r'^[A-Z]{2,3} [0-9A-Z]{3,5}$'
    return bool(re.match(wzor, numer))

def odczytaj_tekst(sciezka):
    obraz = cv2.imread(sciezka)
    obraz_szary = cv2.cvtColor(obraz, cv2.COLOR_BGR2GRAY)
    obraz_przeksztalcony = cv2.threshold(obraz_szary, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
    tekst = pytesseract.image_to_string(obraz_przeksztalcony, config='--oem 3 --psm 6')
    return tekst.strip()

sciezka = 'xd.png'
numer_tablicy = odczytaj_tekst(sciezka)

if spr(numer_tablicy):
    print(f'Numer tablicy rejestracyjnej "{numer_tablicy}" jest poprawny.')
else:
    print(f'Numer tablicy rejestracyjnej "{numer_tablicy}" jest niepoprawny.')
