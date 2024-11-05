# Refactorización: Ir de un punto A a B en el código para mejorarlo.

# Se puede colocar el nombre en la segunda solicitud
# Lo ingresado por el usuario sea lowerCase, de tal forma de comparar minuscula con minuscula
# Más de un turno con el bucle While

ronda = 0
ronda_maxima = 3

nombre1_gano = 0
nombre2_gano = 0

nombre1 = input("¿Como se llamará el jugador 1? ")
nombre2 = input("¿Como se llamará el jugador 2? ")

while ronda < ronda_maxima:

    jugador = ("¡Hola {}! ¿Qué eliges? ¿Piedra, papel o tijeras?: ")
    
    jugador1 = input(jugador.format(nombre1))
    jugador2 = input(jugador.format(nombre2))

    jugador1low = jugador1.lower()
    jugador2low = jugador2.lower()

    condicion1 = jugador1low == "piedra" and jugador2low == "tijeras"
    condicion2 = jugador1low == "papel" and jugador2low == "piedra"
    condicion3 = jugador1low == "tijeras" and jugador2low == "papel"

    #print(jugador1low)
    #print(jugador2low)

    if jugador1low == jugador2low:
        print("¡Ha sido un empate!")
    elif condicion1 or condicion2 or condicion3:
        print("Ha ganado: ", nombre1)
        nombre1_gano +=1
    else:
        print("Ha ganado: ", nombre2)
        nombre2_gano +=1

    ronda += 1

print ("¡Game Over! Has alcanzado el máximo de rondas:", ronda_maxima)
print (nombre1, "gano:", nombre1_gano)
print (nombre2, "gano:", nombre2_gano)


