# Text-to-Speech con OpenAI API

Este proyecto permite convertir texto en audio utilizando la API de OpenAI. Puedes elegir entre diferentes modelos y voces para generar archivos de audio de alta calidad.

## Requisitos

1. Python 3.8 o superior.
2. Una clave API de OpenAI válida.
3. Las librerías requeridas instaladas.

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
   - Introduce el texto que deseas convertir en audio.
   - Selecciona el modelo de generación de voz (por defecto: `tts-1`).
   - Selecciona la voz que prefieres (opciones: `alloy`, `fable`, `nova`, `shimmer`).
   - Define el nombre del archivo de salida (por defecto: `speech.mp3`).

3. **Obtén tu archivo de audio**:
   El archivo de audio generado se guardará en la misma carpeta donde se ejecutó el script.

## Opciones del script

- **Modelos soportados:**
  - `tts-1`: Modelo estándar de texto a voz.
  - `tts-1-hd`: Modelo optimizado para alta calidad.

- **Voces disponibles:**
  - `alloy`
  - `fable`
  - `nova`
  - `shimmer`

## Código principal

### Configuración de la clave API
La clave API se configura directamente en la función `obtener_clave_api`.

### Función principal
La función `text_to_speech` realiza la conversión de texto a audio y guarda el resultado en un archivo de salida.

### Flujo de ejecución
El script solicita la entrada del usuario para generar el archivo de audio deseado.

## Ejemplo de ejecución
```plaintext
¡Bienvenido a la generación de texto a voz con OpenAI!
Escribe el texto que deseas convertir en audio: Hola, este es un ejemplo de texto a voz.
Elige el modelo (tts-1/tts-1-hd): tts-1
Elige la voz (alloy/fable/nova/shimmer): alloy
Nombre del archivo de salida (ejemplo: output.mp3): ejemplo.mp3
Audio generado exitosamente y guardado en: ejemplo.mp3
```

## Notas
- Asegúrate de que tu clave API sea válida y tenga permisos para usar el modelo de texto a voz.
- Si encuentras errores, verifica tu conexión a internet y la configuración del modelo y voz.

## Licencia
Este proyecto se proporciona bajo la [licencia MIT](LICENSE).

