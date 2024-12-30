import os
from openai import OpenAI

# Configuración de la clave API
def obtener_clave_api():
    """Función para obtener la clave API."""
    return "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"

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
