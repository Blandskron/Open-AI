import time
from openai import OpenAI
import random
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("OPENAI_API_KEY")

def initialize_client():
    """Inicializa el cliente de OpenAI utilizando la API Key."""
    if not API_KEY:
        raise ValueError("La clave API no está configurada. Asegúrate de definirla correctamente.")
    return OpenAI(api_key=API_KEY)

def create_thread(client):
    """Crea un nuevo hilo y devuelve el objeto del hilo."""
    thread = client.beta.threads.create()
    print(f"Hilo creado con ID: {thread.id}")
    return thread

def send_message(client, thread_id, message_content):
    """Envía un mensaje a un hilo específico."""
    message = client.beta.threads.messages.create(
        thread_id=thread_id,
        role="user",
        content=message_content
    )
    print("Mensaje enviado al hilo")
    return message

def run_assistant(client, thread_id, assistant_id):
    """Ejecuta el asistente y espera hasta que complete la tarea."""
    run = client.beta.threads.runs.create(
        thread_id=thread_id,
        assistant_id=assistant_id
    )
    print("Ejecutando el asistente...")
    while True:
        run = client.beta.threads.runs.retrieve(
            thread_id=thread_id,
            run_id=run.id
        )
        if run.status == "completed":
            print("La respuesta del asistente está completa")
            break
        time.sleep(1)
    return run

def fetch_assistant_response(client, thread_id):
    """Obtiene y muestra la última respuesta del asistente."""
    messages = client.beta.threads.messages.list(
        thread_id=thread_id,
        order="desc",
        limit=1
    )
    for msg in messages:
        if msg.role == "assistant":
            for content_block in msg.content:
                print("Respuesta del asistente:")
                print(content_block.text.value)

def play_guessing_game():
    """Un juego de adivinanza simple que el asistente puede jugar contigo."""
    print("\nVamos a jugar un juego de adivinanza. Estoy pensando en un número entre 1 y 10.")
    secret_number = random.randint(1, 10)

    while True:
        try:
            guess = int(input("Adivina el número: "))
            if guess < secret_number:
                print("Demasiado bajo. Intenta nuevamente.")
            elif guess > secret_number:
                print("Demasiado alto. Intenta nuevamente.")
            else:
                print("¡Correcto! ¡Ganaste!")
                break
        except ValueError:
            print("Por favor, ingresa un número válido.")

def main():
    client = initialize_client()
    assistant_id = "asst_LODdp3YrW9f74OYCaq5SyHRn"  # ID de tu Amigo Virtual

    thread = create_thread(client)

    # Mensaje inicial amistoso
    send_message(
        client,
        thread.id,
        "¡Hola! Soy tu amigo virtual, siempre dispuesto a conversar y jugar contigo. ¿Qué te gustaría hacer hoy?"
    )

    run = run_assistant(client, thread.id, assistant_id)

    # Mostrar la respuesta del asistente
    fetch_assistant_response(client, thread.id)

    # Iniciar un juego después de la interacción inicial
    play_guessing_game()

if __name__ == "__main__":
    main()
