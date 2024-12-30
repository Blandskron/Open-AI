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

def generate_image(prompt, quality="standard"):
    """Genera una imagen usando la API DALL·E 3."""
    try:
        client = OpenAI(api_key=obtener_clave_api())

        response = client.images.generate(
            model="dall-e-3",
            prompt=prompt,
            quality=quality,
            n=1
        )

        image_url = response.data[0].url
        print(f"Imagen generada: {image_url}")
        return image_url

    except Exception as e:
        print(f"Error al generar la imagen: {e}")
        return None

def main():
    print("¡Bienvenido a la generación de imágenes con DALL·E 3!")
    prompt = input("Describe la imagen que quieres generar: ")
    quality = input("Elige la calidad (standard/hd): ") or "standard"

    image_url = generate_image(prompt, quality)
    if image_url:
        print(f"Tu imagen está disponible en: {image_url}")

if __name__ == "__main__":
    main()
