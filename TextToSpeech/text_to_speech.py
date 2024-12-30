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

def text_to_speech(text, model="tts-1", voice="alloy", output_file="speech.mp3"):
    """Genera un archivo de audio a partir de texto usando la API de OpenAI."""
    try:
        client = OpenAI(api_key=obtener_clave_api())

        with client.audio.speech.with_streaming_response.create(
            model=model,
            voice=voice,
            input=text
        ) as response:
            response.stream_to_file(output_file)

        print(f"Audio generado exitosamente y guardado en: {output_file}")
        return output_file

    except Exception as e:
        print(f"Error al generar el audio: {e}")
        return None

def main():
    print("¡Bienvenido a la generación de texto a voz con OpenAI!")
    text = input("Escribe el texto que deseas convertir en audio: ")
    model = input("Elige el modelo (tts-1/tts-1-hd): ") or "tts-1"
    voice = input("Elige la voz (alloy/fable/nova/shimmer): ") or "alloy"
    output_file = input("Nombre del archivo de salida (ejemplo: output.mp3): ") or "speech.mp3"

    text_to_speech(text, model, voice, output_file)

if __name__ == "__main__":
    main()
