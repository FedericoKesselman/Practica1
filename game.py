import random
# Lista de palabras posibles
words = ["python", "programación", "computadora", "código", "desarrollo", "inteligencia"]

# Elegir una palabra al azar
secret_word = random.choice(words)
# Contador de intentos del usuario 
failed_attempts = 0 
# Lista para almacenar las letras adivinadas
guessed_letters = []

print("¡Bienvenido al juego de adivinanzas!")
print("Estoy pensando en una palabra. ¿Puedes adivinar cuál es?")

# Pedir al usuario que ingrese dificultad 
difficulty = int(input("Dificultad del juego (1: Facil, 2: Medio, 3: Dificil): ")) 

if difficulty == 3: 
    # En dificil se mantiene codigo anterior
    word_displayed = "_" * len(secret_word)
elif difficulty == 2:
    # Se muestra primera y ultima letra. Son agregadas a la lista de letras
    word_displayed = secret_word[0] + "_" * (len(secret_word)-2) + secret_word[-1]
    guessed_letters.append(secret_word[0])
    guessed_letters.append(secret_word[-1])
else:
    # Se muestran vocales. Son agregadas a la lista de letras
    word_displayed = "".join([letter if letter in 'aeiou' else "_" for letter in secret_word]) 

    for letter in secret_word:
        if letter in 'aeiou':
                guessed_letters.append(letter)

print(f"Palabra: {word_displayed}")

while failed_attempts < 10:
    # Pedir al jugador que ingrese una letra
    letter = input("Ingresa una letra: ").lower()

     # Verificar si la letra ya ha sido adivinada
    if letter in guessed_letters:
        print("Ya cuentas con esa letra. Intenta con otra.")
        continue
    
    if letter == "":
        print("Error. No se ingreso ninguna letra.")
        continue

    # Agregar la letra a la lista de letras adivinadas
    guessed_letters.append(letter)

    # Verificar si la letra está en la palabra secreta
    if letter in secret_word:
        print("¡Bien hecho! La letra está en la palabra.")
    else:
        print("Lo siento, la letra no está en la palabra.")
        failed_attempts += 1 

    # Mostrar la palabra parcialmente adivinada
    letters = []
    for letter in secret_word:
        if letter in guessed_letters:
            letters.append(letter)
        else:
            letters.append("_")

    word_displayed = "".join(letters)
    print(f"Palabra: {word_displayed}")
    # Verificar si se ha adivinado la palabra completa
    if word_displayed == secret_word:
        print(f"¡Felicidades! Has adivinado la palabra secreta: {secret_word}")
        break
else:
    print("¡Oh no! Has agotado tus 10 intentos.")
    print(f"La palabra secreta era: {secret_word}")
