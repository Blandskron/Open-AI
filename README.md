# Proyecto AmigoVirtual: Interacción con OpenAI API

Este repositorio contiene múltiples ejemplos prácticos que demuestran cómo interactuar con las APIs de OpenAI para tareas como generación de texto, generación de imágenes, transcripción de audio y conversión de texto a voz. Además, incluye un chatbot interactivo llamado **AmigoVirtual** que combina capacidades de conversación y juegos simples.

## Tabla de Contenidos

- [Requisitos](#requisitos)
- [Instalación](#instalación)
- [Componentes del Proyecto](#componentes-del-proyecto)
  - [AmigoVirtual: Chat Continuo](#amigovirtual-chat-continuo)
  - [Generación de Imágenes](#generación-de-imágenes)
  - [Transcripción de Audio](#transcripción-de-audio)
  - [Texto a Voz](#texto-a-voz)
  - [AmigoVirtual con Juego](#amigovirtual-con-juego)
- [Ejemplo de Uso](#ejemplo-de-uso)
- [Notas](#notas)
- [Licencia](#licencia)

## Requisitos

1. Python 3.8 o superior.
2. Una clave API de OpenAI válida.
3. Las librerías necesarias instaladas.

## Instalación

1. Clona este repositorio:
   ```bash
   git clone https://github.com/tu-usuario/proyecto-amigovirtual.git
   cd proyecto-amigovirtual
   ```

2. Instala las dependencias:
   ```bash
   pip install openai
   ```

## Componentes del Proyecto

### AmigoVirtual: Chat Continuo
- **Archivo:** `amigo_virtual.py`
- **Descripción:** Implementa un chatbot interactivo que mantiene el historial de conversación y responde de manera amigable y coherente.

### Generación de Imágenes
- **Archivo:** `generate_image.py`
- **Descripción:** Genera imágenes a partir de descripciones textuales usando la API DALL·E 3.

### Transcripción de Audio
- **Archivo:** `transcribe_audio.py`
- **Descripción:** Convierte archivos de audio en texto utilizando el modelo Whisper de OpenAI.

### Texto a Voz
- **Archivo:** `text_to_speech.py`
- **Descripción:** Convierte texto en archivos de audio utilizando la API de texto a voz de OpenAI, con soporte para múltiples modelos y voces.

### AmigoVirtual con Juego
- **Archivo:** `amigo_virtual_game.py`
- **Descripción:** Combina la funcionalidad de conversación continua con un simple juego de adivinanza en el que el usuario intenta adivinar un número entre 1 y 10.

## Ejemplo de Uso

### 1. Ejecutar AmigoVirtual
```bash
python amigo_virtual.py
```
Interactúa con el asistente escribiendo mensajes. Para salir, escribe "salir" o "adiós".

### 2. Generar una Imagen
```bash
python generate_image.py
```
Describe la imagen que deseas generar y selecciona la calidad. Obtendrás un enlace a la imagen generada.

### 3. Transcribir un Audio
```bash
python transcribe_audio.py
```
Proporciona la ruta de un archivo de audio (ejemplo: `speech.mp3`) para obtener su transcripción.

### 4. Convertir Texto a Voz
```bash
python text_to_speech.py
```
Escribe un texto, selecciona el modelo y la voz, y obtendrás un archivo de audio generado.

### 5. Jugar con AmigoVirtual
```bash
python amigo_virtual_game.py
```
Conversarás con AmigoVirtual y luego podrás jugar un juego de adivinanza.

## Notas

- Asegúrate de configurar correctamente la clave API en cada archivo.
- Verifica que los archivos necesarios (como audio o configuraciones) estén en las rutas adecuadas.
- Cada archivo incluye su propio README específico para más detalles.

## Licencia

Este proyecto se proporciona bajo la [licencia MIT](LICENSE).

