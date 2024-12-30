import os
from openai import OpenAI

# Configuración de la clave API
def obtener_clave_api():
    """Función para obtener la clave API."""
    return "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"

def transcribe_audio(file_path):
    """Transcribe un archivo de audio usando la API Whisper."""
    try:
        client = OpenAI(api_key=obtener_clave_api())

        with open(file_path, "rb") as audio_file:
            response = client.audio.transcriptions.create(
                model="whisper-1",
                file=audio_file
            )

        print("Transcripción:")
        print(response.text)
        return response.text

    except Exception as e:
        print(f"Error al transcribir el audio: {e}")
        return None

def main():
    print("¡Bienvenido a la transcripción de audio con Whisper!")
    file_path = input("Por favor, proporciona la ruta del archivo de audio (ejemplo: speech.mp3): ")

    if not os.path.exists(file_path):
        print("El archivo no existe. Por favor verifica la ruta.")
        return

    transcribe_audio(file_path)

if __name__ == "__main__":
    main()
