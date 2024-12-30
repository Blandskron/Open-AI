# AmigoVirtual: Chat Continuo con OpenAI API

Este proyecto implementa un chatbot llamado **AmigoVirtual**, utilizando la API de OpenAI para proporcionar una experiencia de conversación continua, amigable y divertida. AmigoVirtual siempre está dispuesto a interactuar y jugar contigo.

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
   - Escribe tus mensajes en la consola.
   - AmigoVirtual responderá y mantendrá el contexto de la conversación.

3. **Finaliza la conversación**:
   - Escribe "salir", "adiós" o "exit" para terminar la interacción.

## Opciones del script

- **Modelo utilizado:**
  - `gpt-4o`: Modelo avanzado para generar respuestas contextuales y naturales.

- **Historial de mensajes:**
  - AmigoVirtual mantiene el historial de la conversación para dar respuestas coherentes.

## Código principal

### Configuración de la clave API
La clave API se configura directamente en la función `obtener_clave_api`.

### Función principal
La función `chat_with_model` gestiona el flujo de la conversación, incluyendo la captura de mensajes del usuario y las respuestas generadas por el modelo.

### Flujo de ejecución
El script inicia con un mensaje introductorio y permite conversaciones continuas hasta que el usuario decide finalizar.

## Ejemplo de ejecución
```plaintext
¡Hola! Soy AmigoVirtual. Puedes escribirme algo para comenzar a conversar o jugar.
Tú: Hola, ¿cómo estás?
AmigoVirtual: ¡Hola! Estoy genial, gracias por preguntar. ¿En qué puedo ayudarte hoy?
Tú: ¿Quieres jugar algo?
AmigoVirtual: ¡Claro! Dime, ¿qué juego te gustaría jugar?
Tú: salir
AmigoVirtual: ¡Hasta luego! Fue un placer conversar contigo.
```

## Notas
- Asegúrate de que tu clave API sea válida y tenga permisos para usar el modelo ChatCompletion.
- Si encuentras errores, verifica tu conexión a internet y el formato de los mensajes.

## Licencia
Este proyecto se proporciona bajo la [licencia MIT](LICENSE).

