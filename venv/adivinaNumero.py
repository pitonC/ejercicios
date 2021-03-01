import random

numero = random.randrange(1,50)
adivi = int(input("adivina un numero entre 1 y 50: "))

while adivi != numero:
    if adivi < numero:
        print("da un valor mas alto. reintentalo")
        adivi = int (input("\nAdivina un numero entre 1 y 50: "))
    else:
        print("da un valor mas bajo. reintentalo")
        adivi = int(input("\nAdivina un numero entre 1 y 50: "))

        print("Has ganado. adivinastes correctamente")