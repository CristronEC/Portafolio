# Opciones del juego
opciones = ["piedra", "papel", "tijera"]

# Función para obtener la elección del jugador
def eleccion_jugador():
    eleccion = input("Elige piedra, papel o tijera: ").lower()
    while eleccion not in opciones:
        eleccion = input("Opción no válida. Elige piedra, papel o tijera: ").lower()
    return eleccion

# Juego principal
def jugar():
    print("Bienvenido a Piedra, Papel o Tijera!")
    jugador = eleccion_jugador()