import random  # Importamos el módulo random para generar elecciones aleatorias de la computadora

# Opciones del juego
opciones = ["piedra", "papel", "tijera"]

# Función para obtener la elección del jugador
def eleccion_jugador():
    """
    Solicita al jugador que elija entre piedra, papel o tijera.
    Valida que la entrada sea válida, repitiendo la solicitud si es necesario.
    """
    eleccion = input("Elige piedra, papel o tijera: ").lower()
    while eleccion not in opciones:  # Aseguramos que el jugador elija una opción válida
        eleccion = input("Opción no válida. Elige piedra, papel o tijera: ").lower()
    return eleccion

# Función para que la computadora elija aleatoriamente
def eleccion_computadora():
    """
    La computadora elige aleatoriamente entre piedra, papel o tijera.
    """
    return random.choice(opciones)

# Función para determinar si el jugador gana
def jugador_gana(jugador, computadora):
    """
    Determina si el jugador gana comparando las elecciones.
    - Piedra vence a Tijera.
    - Tijera vence a Papel.
    - Papel vence a Piedra.
    """
    if (jugador == "piedra" and computadora == "tijera") or \
       (jugador == "tijera" and computadora == "papel") or \
       (jugador == "papel" and computadora == "piedra"):
        return True
    return False

# Juego principal
def jugar():
    """
    Ejecución principal del juego de Piedra, Papel o Tijera.
    Incluye un bucle para manejar empates y determinar si el jugador desea volver a jugar.
    """
    print("¡Bienvenido a Piedra, Papel o Tijera!")

    while True:  # Bucle principal del juego
        # Elecciones del jugador y la computadora
        jugador = eleccion_jugador()
        computadora = eleccion_computadora()
        
        print(f"Tú elegiste: {jugador}")
        print(f"La computadora eligió: {computadora}")

        # Condición para manejar empates
        if jugador == computadora:
            print("¡Empate! Juguemos otra vez.")
            continue  # Vuelve al inicio del bucle si hay empate

        # Condición para determinar el ganador
        if jugador_gana(jugador, computadora):
            print("¡Ganaste!")
        else:
            print("Perdiste. ¡Mejor suerte la próxima vez!")

        # Preguntar al jugador si desea volver a jugar
        jugar_otra_vez = input("¿Quieres jugar otra vez? (sí/no): ").lower()
        if jugar_otra_vez != "sí":
            print("Gracias por jugar. ¡Hasta la próxima!")
            break  # Sale del bucle si el jugador no desea continuar

# Llamar al juego
jugar()
