# AmigoVirtual: Conversación y Juego de Adivinanza con OpenAI API

Este proyecto combina las capacidades de interacción continua de OpenAI API con un simple y divertido juego de adivinanza. **AmigoVirtual** es un asistente dispuesto a conversar y jugar contigo en cualquier momento.

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

2. **Interactúa con AmigoVirtual**:
   - Inicia una conversación y recibe respuestas del asistente.

3. **Juega al juego de adivinanza**:
   - Después de interactuar con el asistente, podrás jugar un simple juego en el que intentas adivinar un número entre 1 y 10.

4. **Finaliza la conversación**:
   - Escribe "salir" o "adiós" para terminar la interacción con el asistente.

## Opciones del script

- **Modelo utilizado:**
  - `gpt-4o`: Modelo avanzado para generar respuestas contextuales y naturales.

- **Juego de adivinanza:**
  - Genera un número aleatorio entre 1 y 10.
  - El usuario intenta adivinar el número basado en pistas proporcionadas.

## Código principal

### Configuración de la clave API
La clave API se configura directamente en la variable `API_KEY`.

### Función principal
1. La función `initialize_client` configura la conexión con OpenAI.
2. `create_thread`, `send_message`, y `run_assistant` manejan la conversación con el asistente.
3. `play_guessing_game` inicia un simple juego de adivinanza.

## Ejemplo de ejecución
```plaintext
¡Hola! Soy tu amigo virtual, siempre dispuesto a conversar y jugar contigo. ¿Qué te gustaría hacer hoy?
Tú: Hola, ¿qué tal?
AmigoVirtual: ¡Hola! Estoy genial, gracias por preguntar. ¿Cómo puedo ayudarte hoy?

Vamos a jugar un juego de adivinanza. Estoy pensando en un número entre 1 y 10.
Adivina el número: 5
Demasiado bajo. Intenta nuevamente.
Adivina el número: 8
¡Correcto! ¡Ganaste!
```

## Notas
- Asegúrate de que tu clave API sea válida y tenga permisos para usar el modelo ChatCompletion.
- Si encuentras errores, verifica tu conexión a internet y el formato de los mensajes.

## Licencia
Este proyecto se proporciona bajo la [licencia MIT](LICENSE).

