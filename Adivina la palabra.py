import random


def adivina_el_numero (x):
    print("     ---------------------     ")
    print("----| Bienvenido al juego |----")
    print("     ---------------------     ")
    print(f"Seleccione un número entre el 1 y el {x} para que la computadora trate de adivinarlo".upper())
    print()

    limite_superior = x
    limite_inferior = 1
    respuesta = " "

    while respuesta != "c":
        #Generar una predicción
        if limite_inferior != limite_superior:
            predicción = random.randint(limite_inferior, limite_superior)
        else:
            predicción = limite_superior

        #Respuesta del usuario
        respuesta = input(f"Mi predicción es {predicción}.  Es muy alta, ingres(A).  Es muy baja, ingresa(B).  Si es la correcta, ingresa(C). :   ").lower()

        #Cambiar los limites dependiendo a la respuesta del usuario
        if respuesta == "A":
            limite_superior = predicción - 1
        elif respuesta == "B":
            limite_inferior = predicción + 1

    print(f"La computadora pudo adivinar el numero que habias seleccionado: {x}")

adivina_el_numero(20)

