# Chat-Bot de atención DIAD

- Título: Embedchain-Chat-Bot-DIAD--V1
- Versión: 1.0
- Utilidad: Soporte al cliente

## Descripción

Es un _chatbot_ que permite a los usuarios obtener respuestas a sus preguntas basándose en la información contenida en el archivo `PDF` especificado. 

El _chatbot_ se presenta en una interfaz web amigable que facilita la interacción con los usuarios, y utiliza un modelo de lenguaje natural para generar respuestas coherentes y precisas en el contexto del documento.

## Requisitos

### Dependencias

Se pueden consultar a más detalle los paquetes necesarios del proyecto en el archivo [**requirements.txt**](requirements.txt) de este repositorio.
Puede realizar la instalación de las dependencias con `pip` del siguiente modo:

```bash
pip install -r requirements.txt
```
### Base de conocimientos

Esta versión del _chatbot_ requiere un archivo en formato `PDF` que contenga la información que se desea poner a disposición de los usuarios.

> [!WARNING]
> Se debe actualizar el nombre del archivo que se desea utilizar en [**main.py**](main.py).

### API de Inteligencia Artificial

Es necesario contar con una clave de la API de OpenAI, la cual se debe establecer como la  variable de entorno `OPENAI_API_KEY`. Para realizar la configuración puedes utilizar el siguiente código:

```python
import os
os.environ["OPENAI_API_KEY"] = "<YOUR_API_KEY>"
```
## Funcionamiento

Este código crea una aplicación web de _chatbot_ para responder preguntas sobre el contenido de un archivo `PDF`. Aquí's un desglose del funcionamiento:

### Carga y procesamiento de PDF

Se utiliza la biblioteca [Embedchain](https://github.com/embedchain) para cargar y procesar el archivo `PDF` especificado, la cual extrae información relevante del documento, como texto, entidades y relaciones entre ellas, y crea una representación interna del conocimiento contenido en el documento.

### Aplicación web y recepción de preguntas

Se crea una aplicación web simple usando [Flask](https://flask.palletsprojects.com/en/3.0.x/) y se definen rutas para manejar las interacciones del usuario:
- La ruta raíz `( / )` renderiza la página `HTML` de la interfaz del chatbot.
- La ruta `( /chat )` recibe preguntas del usuario a través de una solicitud `POST`.

### Generación de respuestas

- Se recibe la pregunta del usuario en formato `JSON` y se añade la instrucción de que la respuesta debe basarse en el documento consultado.
- Se utiliza la instancia de **Embedchain** que se conecta a la API de **OpenAI** para generar una respuesta a la pregunta.
- Si todo es correcto, la respuesta generada se devuelve al usuario en formato `JSON`; caso contrario se muestra un mensaje de error.

## Resultados

Este proyecto genera una interfaz web que permite a los usuarios la interacción con un _chatbot_ capaz de procesar un documento `PDF`, recibir preguntas en lenguaje natural y consultar el conocimiento del documento para generar respuestas relevantes y coherentes. 

Además cuenta con características adicionales que aportan valor en la usabilidad del _chatbot_, las cuales se detallan a continuación:

- **Generación de respuestas relevantes:** El _chatbot_ genera respuestas completas e informativas a las preguntas del usuario, utilizando el conocimiento extraído del `PDF` y adaptando el lenguaje a un estilo natural y conversacional.
- **Historial de conversaciones:** Las interacciones con el _chatbot_ se almacenan localmente, permitiendo al usuario revisar las conversaciones anteriores, consultar información específica o eliminar conversaciones que ya no sean necesarias.
- **Temas personalizables:** El usuario puede elegir entre un tema claro u oscuro para la interfaz del _chatbot_, personalizando la experiencia visual según sus preferencias.
- **Uso de avatares:** Se integran avatares en la interfaz para representar al usuario y al _chatbot_ durante la conversación, aportando un toque más humano y dinámico a la interacción.
- **Uso de la información:** El usuario puede copiar fácilmente el texto de una respuesta del _chatbot_ al portapapeles, permitiendo guardar o compartir información relevante de manera rápida y sencilla.

