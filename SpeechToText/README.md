# Transcripción de Audio con OpenAI Whisper API

Este proyecto permite transcribir archivos de audio utilizando la API Whisper de OpenAI. Es ideal para convertir audio en texto de manera eficiente y precisa.

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
   - Proporciona la ruta al archivo de audio que deseas transcribir (ejemplo: `speech.mp3`).

3. **Obtén tu transcripción**:
   - El texto transcrito del archivo de audio se mostrará en la terminal.

## Opciones del script

- **Modelo soportado:**
  - `whisper-1`: Modelo de OpenAI diseñado para transcribir audio con alta precisión en múltiples idiomas.

## Código principal

### Configuración de la clave API
La clave API se configura directamente en la función `obtener_clave_api`.

### Función principal
La función `transcribe_audio` procesa un archivo de audio y devuelve la transcripción.

### Flujo de ejecución
El script solicita la ruta del archivo de audio y verifica su existencia antes de intentar transcribirlo.

## Ejemplo de ejecución
```plaintext
¡Bienvenido a la transcripción de audio con Whisper!
Por favor, proporciona la ruta del archivo de audio (ejemplo: speech.mp3): speech.mp3
Transcripción:
Este es el texto transcrito del archivo de audio.
```

## Notas
- Asegúrate de que tu clave API sea válida y tenga permisos para usar el modelo Whisper.
- Si encuentras errores, verifica tu conexión a internet y la ruta del archivo de audio.

## Licencia
Este proyecto se proporciona bajo la [licencia MIT](LICENSE).

