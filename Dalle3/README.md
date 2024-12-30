# Generación de Imágenes con OpenAI DALL·E 3 API

Este proyecto permite generar imágenes a partir de descripciones textuales utilizando la API DALL·E 3 de OpenAI. Puedes personalizar la calidad de las imágenes y obtener el enlace directo a la imagen generada.

## Requisitos

1. Python 3.8 o superior.
2. Una clave API de OpenAI válida.
3. Las librerías necesarias instaladas.

## Instalación

1. **Clona el repositorio** o guarda este script en tu proyecto.
2. **Instala las dependencias necesarias:**
   ```bash
   pip install openai
   ```

## Uso

1. **Ejecuta el script**:
   ```bash
   python nombre_del_archivo.py
   ```

2. **Sigue las instrucciones en pantalla**:
   - Describe la imagen que deseas generar.
   - Elige la calidad de la imagen (opciones: `standard` o `hd`).

3. **Obtén tu imagen**:
   - La URL de la imagen generada se mostrará en la terminal.

## Opciones del script

- **Modelo utilizado:**
  - `dall-e-3`: Modelo avanzado para generación de imágenes a partir de texto.

- **Calidad disponible:**
  - `standard`: Calidad estándar.
  - `hd`: Alta calidad.

## Código principal

### Configuración de la clave API
La clave API se configura directamente en la función `obtener_clave_api`.

### Función principal
La función `generate_image` genera la imagen según el prompt proporcionado por el usuario y devuelve la URL de la imagen generada.

### Flujo de ejecución
El script solicita un prompt (descripción de la imagen) y una calidad, y luego genera la imagen utilizando la API de OpenAI.

## Ejemplo de ejecución
```plaintext
¡Bienvenido a la generación de imágenes con DALL·E 3!
Describe la imagen que quieres generar: Un paisaje de montaña con un lago al atardecer.
Elige la calidad (standard/hd): hd
Imagen generada: https://openai-generated-images.com/example-image-url
Tu imagen está disponible en: https://openai-generated-images.com/example-image-url
```

## Notas
- Asegúrate de que tu clave API sea válida y tenga permisos para usar la API DALL·E 3.
- Si encuentras errores, verifica tu conexión a internet y el formato del prompt.

## Licencia
Este proyecto se proporciona bajo la [licencia MIT](LICENSE).

