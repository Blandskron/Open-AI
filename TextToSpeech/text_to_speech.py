import os
from openai import OpenAI

# Configuración de la clave API
def obtener_clave_api():
    """Función para obtener la clave API."""
    return "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"

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
