import random

vida = 100
magia = 50
vida_enemigo = 100
turno = 1

while vida > 0 and vida_enemigo > 0:

    print("Turno", turno)
    print("Tu vida:", vida, "| Magia:", magia)
    print("Vida enemigo:", vida_enemigo)

    print("Elegi")
    print("1 - pegar")
    print("2 - magia fuerte")
    print("3 - curarte")

    op = input("> ")

    if op == "1":
        d = random.randint(8, 18)
        vida_enemigo -= d
        print("le pegaste y sacaste", d)

    elif op == "2":
        if magia >= 15:
            d = random.randint(20, 35)
            vida_enemigo -= d
            magia -= 15
            print("tiraste magia y sacaste", d)
        else:
            print("no te alcanza el magia")

    elif op == "3":
        if magia >= 10:
            vida += 15
            magia -= 10
            print("te curaste un poco")
        else:
            print("sin magia, no podes curarte")

    else:
        print("no hiciste nada")

    if vida_enemigo <= 0:
        print("Ganaste ")
        break

    print("Ahora va el enemigo")

    e = random.randint(1, 2)

    if e == 1:
        d = random.randint(8, 18)
        vida -= d
        print("te pego y te saco", d)
    else:
        d = random.randint(15, 25)
        vida -= d
        print("te tiro magia y te saco", d)

    if vida <= 0:
        print("Perdiste ")

    turno += 1