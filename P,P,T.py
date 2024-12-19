import random  # Importamos el módulo random para generar elecciones aleatorias de la computadora

# Opciones del juego
opciones = ["piedra", "papel", "tijera"]  # Definimos las opciones posibles del juego en una lista

# Función para obtener la elección del jugador
def eleccion_jugador(jugador_numero=1):
    """
    Solicita al jugador que elija entre piedra, papel o tijera.
    Valida que la entrada sea válida, repitiendo la solicitud si es necesario.
    """
    eleccion = input(f"Jugador {jugador_numero}, elige piedra, papel o tijera: ").lower()  # Solicita la elección del jugador y la convierte a minúsculas
    while eleccion not in opciones:  # Aseguramos que el jugador elija una opción válida
        eleccion = input(f"Jugador {jugador_numero}, opción no válida. Elige piedra, papel o tijera: ").lower()  # Si no es válida, pide otra entrada
    return eleccion  # Retorna la elección válida del jugador

# Función para que la computadora elija aleatoriamente
def eleccion_computadora():
    """
    La computadora elige aleatoriamente entre piedra, papel o tijera.
    """
    return random.choice(opciones)  # La computadora elige aleatoriamente entre las opciones definidas

# Función para determinar si el jugador gana
def jugador_gana(jugador, computadora):
    """
    Determina si el jugador gana comparando las elecciones.
    - Piedra vence a Tijera.
    - Tijera vence a Papel.
    - Papel vence a Piedra.
    """
    # Compara las elecciones del jugador y la computadora para determinar si el jugador gana
    if (jugador == "piedra" and computadora == "tijera") or \
       (jugador == "tijera" and computadora == "papel") or \
       (jugador == "papel" and computadora == "piedra"):
        return True  # Si el jugador gana, retorna True
    return False  # Si el jugador no gana, retorna False

# Juego principal
def jugar():
    """
    Ejecución principal del juego de Piedra, Papel o Tijera.
    Incluye un bucle para manejar empates y determinar si el jugador desea volver a jugar.
    """
    print("¡Bienvenido a Piedra, Papel o Tijera!")  # Mensaje de bienvenida al jugador

    # Preguntar si desea jugar con computadora o multijugador
    while True:
        modo_juego = input("¿Quieres jugar con la computadora o multijugador? (escribe 'computadora' o 'multijugador'): ").lower()
        if modo_juego == "computadora" or modo_juego == "multijugador":
            break
        else:
            print("Opción no válida. Por favor, escribe 'computadora' o 'multijugador'.")

    while True:  # Bucle principal del juego que permite jugar varias veces
        # Elecciones de los jugadores
        jugador1 = eleccion_jugador(1)  # Obtiene la elección del jugador 1

        if modo_juego == "computadora":
            computadora = eleccion_computadora()  # Obtiene la elección de la computadora
            print(f"Tú (Jugador 1) elegiste: {jugador1}")  # Muestra la elección del jugador 1
            print(f"La computadora eligió: {computadora}")  # Muestra la elección de la computadora
        else:
            # Modo multijugador: el segundo jugador elige
            jugador2 = eleccion_jugador(2)  # Obtiene la elección del jugador 2
            print(f"Jugador 1 eligió: {jugador1}")  # Muestra la elección del jugador 1
            print(f"Jugador 2 eligió: {jugador2}")  # Muestra la elección del jugador 2
            computadora = jugador2  # En modo multijugador, el segundo jugador es la "computadora" virtual

        # Condición para manejar empates
        if jugador1 == computadora:  # Si las elecciones son iguales, es un empate
            print("¡Empate! Juguemos otra vez.")  # Mensaje de empate
            continue  # Vuelve al inicio del bucle y permite jugar otra vez

        # Condición para determinar el ganador
        if jugador_gana(jugador1, computadora):  # Si el jugador 1 gana, se ejecuta el siguiente bloque
            print("¡Jugador 1 ganó!")  # Mensaje de victoria para el jugador 1
        else:  # Si el jugador 1 no gana, entonces el jugador 2 gana (o la computadora)
            if modo_juego == "computadora":
                print("Perdiste. ¡Mejor suerte la próxima vez!")  # Mensaje de derrota para el jugador 1 contra la computadora
            else:
                print("¡Jugador 2 ganó!")  # Mensaje de derrota para el jugador 1 en modo multijugador

        # Preguntar al jugador si desea volver a jugar
        while True:
            jugar_otra_vez = input("¿Quieres jugar otra vez? (sí/no): ").lower()  # Solicita la respuesta del jugador
            if jugar_otra_vez == "sí" or jugar_otra_vez == "no":
                break
            else:
                print("Respuesta no válida. Por favor, responde con 'sí' o 'no'.")

        if jugar_otra_vez != "sí":  # Si el jugador no responde "sí", termina el juego
            print("Gracias por jugar. ¡Hasta la próxima!")  # Mensaje de despedida
            break  # Sale del bucle principal y termina el juego

        # Si el jugador eligió "sí", preguntar nuevamente si quiere jugar con la computadora o multijugador
        while True:
            modo_juego = input("¿Quieres jugar con la computadora o multijugador? (escribe 'computadora' o 'multijugador'): ").lower()
            if modo_juego == "computadora" or modo_juego == "multijugador":
                break
            else:
                print("Opción no válida. Por favor, escribe 'computadora' o 'multijugador'.")

# Llamar al juego
jugar()  # Llama a la función 'jugar' para iniciar el juego
