import os
from openai import OpenAI
from dotenv import load_dotenv

# Cargar las variables de entorno desde el archivo .env
load_dotenv()

def obtener_clave_api():
    """Función para obtener la clave API desde las variables de entorno."""
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise ValueError("La clave API no está configurada. Asegúrate de definir OPENAI_API_KEY en tu archivo .env.")
    return api_key

def chat_with_model():
    """Interactúa con ChatCompletion API en un bucle para permitir conversaciones continuas."""
    try:
        client = OpenAI(api_key=obtener_clave_api())

        messages = [
            {"role": "system", "content": "Te llamas AmigoVirtual, siempre amable y dispuesto a jugar."}
        ]

        print("¡Hola! Soy AmigoVirtual. Puedes escribirme algo para comenzar a conversar o jugar.")

        while True:
            user_input = input("Tú: ")
            if user_input.lower() in ["salir", "adiós", "exit"]:
                print("AmigoVirtual: ¡Hasta luego! Fue un placer conversar contigo.")
                break

            # Añadir el mensaje del usuario al historial
            messages.append({"role": "user", "content": user_input})

            # Obtener la respuesta del modelo
            response = client.chat.completions.create(
                model="gpt-4o",  # Modelo a utilizar
                messages=messages,
                max_tokens=100,
                temperature=0.7
            )

            # Extraer y mostrar la respuesta del asistente
            assistant_message = response.choices[0].message.content
            print(f"AmigoVirtual: {assistant_message}")

            # Añadir la respuesta del asistente al historial
            messages.append({"role": "assistant", "content": assistant_message})

    except Exception as e:
        print(f"Error al interactuar con el modelo: {e}")

if __name__ == "__main__":
    chat_with_model()
