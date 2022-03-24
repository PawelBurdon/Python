import random

def losuj_az():
    mala = random.randint(97, 122)
    return chr(mala)

def losuj_AZ():
    duza = random.randint(65, 90)
    return chr(duza)

def losuj_09():
    cyfry = random.randint(0, 9)
    return str(cyfry)

def losuj_agenci():
    agenci = random.randint(33, 42)
    return chr(agenci)

def generuj():
    y = input("Dlugosc hasla: ")

    while y.isdigit() == False:
        print("Podaj poprawna wartosc!!!")
        y = input("\nDlugosc hasla: ")

    haslo = ""

    for z in range(int(y)):
        znak = random.randint(1, 4)
        if znak == 1:
            haslo += losuj_az()
        elif znak == 2:
            haslo += losuj_AZ()
        elif znak == 3:
            haslo += losuj_09()
        elif znak == 4:
            haslo += losuj_agenci()

    f.write("\nTwoje haslo = " + haslo)


