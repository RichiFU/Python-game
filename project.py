import random
import re
import csv
import os

def main():
    vidas = 10
    print("🎯 Bienvenido al juego de adivinanza 🎯")

    acerto_numero, vidas_restantes = adivinar_numero(vidas)
    if not acerto_numero:
        print("😢 Has perdido. Fin del juego.")
        return

    print("🎉 ¡Correcto! Pasas a la adivinanza final...\n")


    if preguntar_adivinanza(vidas_restantes):
        print("🏆 ¡Felicidades, ganaste el juego!")
    else:
        print("❌ Fallaste la adivinanza. Fin del juego.")


    print("\n📁 El historial se guardó en:")
    print(os.path.abspath("historial.csv"))

    mostrar_historial()


def adivinar_numero(vidas):
    # Numero al Azar del 1 al 10
    numero_objetivo = random.randint(1,10)
    print(numero_objetivo)


    while vidas > 0:
        guess = input(f"Adivina el número (1-10). Te quedan {vidas} vidas: ")
        # Si el numero ingresado no es del 1 al 10, el bucle continua
        if not re.fullmatch(r"[1-9]|10", guess):
            print("Entrada inválida. Intenta nuevamente.")
            continue

        try:
            # Se transforma el numero ingresado a entero.
            guess = int(guess)
        except ValueError:
            print("Entrada inválida, debe ser un número.")
            continue

        # Se crea una variable en donde se guarda el resultado si la suposicion es igual al numero objetivo
        correcta = guess == numero_objetivo
        # Se le pasan los argumentos a la funcion que guarda en un 'csv'
        guardar_jugada("numero", guess, correcta)

        if correcta:
            # Devuelvo true y vidas ocupadas a main()
            return True, vidas
        else:
            print("❌ Número incorrecto.")
            # Por cada respuesta incorrecta se resta una vida
            vidas -= 1

    return False


def preguntar_adivinanza(vidas):
    adivinanzas = {
        "Tiene dientes pero no muerde": "peine",
        "Vuela sin alas y llora sin ojos": "nube",
        "Llena de agujeros pero retiene agua": "esponja",
        "Si me nombras desaparezco, ¿quién soy?": "silencio",
        "No tiene boca y te dice la verdad": "espejo",
        "Cuanto más seco, más moja": "toalla"
    }

    # Utilizo unpacked para extraer las preguntas y respuestas del objeto adivinanzas
    pregunta, respuesta = random.choice(list(adivinanzas.items()))
    print("❓ Adivinanza: ", pregunta)

    while vidas > 0:
        respuesta_usuario = input(f"Tu respuesta (vidas restantes: {vidas}): ").strip().lower()
        # Busca la palabra clave dentro de la respuesta del usuario usando regex
        correcta = re.search(rf"\b{respuesta}\b", respuesta_usuario)

        guardar_jugada("adivinanza", respuesta_usuario, bool(correcta))

        if correcta:
            return True
        else:
            print("❌ Incorrecto.")
            vidas -= 1

    return False  # perdió todas las vidas


def guardar_jugada(tipo, respuesta, correcta):
    try:
        with open("historial.csv", "a", newline='') as file:
            writer = csv.writer(file)
            writer.writerow([tipo, respuesta, "correcto" if correcta else "incorrecto"])
    except IOError as e:
        print(f"⚠️ Error al guardar en el archivo CSV: {e}")


def mostrar_historial():
    archivo = "historial.csv"
    try:
        with open(archivo, newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            print("\n📜 Historial de jugadas:")
            for fila in reader:
                # fila es una lista, por ejemplo: ['numero', '5', 'incorrecto']
                print(", ".join(fila))
    except FileNotFoundError:
        print("⚠️ No hay historial para mostrar aún.")


# Funciones testeables con pytest:

def es_numero_valido(guess):
    """Valida si el input es un número entre 1 y 10."""
    return re.fullmatch(r"[1-9]|10", guess)


def comparar_respuesta(respuesta_correcta, respuesta_usuario):
    """Evalua si la respuesta del usuario contiene la palabra clave correcta."""
    return bool(re.search(rf"\b{respuesta_correcta}\b", respuesta_usuario.strip().lower()))


def resultado_a_texto(correcta):
    """Convierte un booleano a texto: 'correcto' o 'incorrecto'."""
    return "correcto" if correcta else "incorrecto"

if __name__ == "__main__":
    main()
