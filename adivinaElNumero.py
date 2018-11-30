import random
intentosRealizados = 1
intentosTotales = 6

print ("Escribe tu nombre:")
nombre = input()

print ("Hola " + nombre + ", intenta adivinar mi numero.")

numeroAdivinar = random.randint(1, 20)
print("Mi número esta entre el 1 y el 20")


while intentosRealizados < intentosTotales:
    print("Que numero estoy pensando?")
    numeroStr  = input()
    numero = int(numeroStr)

    if numero == numeroAdivinar:
        print ("Felicidades .... ¡¡¡ Adivinaste en " + str(intentosRealizados) + " intentos !!!")
        break
    else:
        if numero < numeroAdivinar:
            print ("Mi numero es mas grande ...")
        else:
            print ("Mi numero es menor")

    intentosRealizados = intentosRealizados + 1
    numero = -1

if numero == -1:
    print("Sorrrry yo ... Mas suerte para la próxima, mi numero era: " + str(numeroAdivinar))
        

