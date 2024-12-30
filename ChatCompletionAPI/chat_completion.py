import os
from openai import OpenAI

# Configuración de la clave API
def obtener_clave_api():
    """Función para obtener la clave API."""
    return "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"

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
