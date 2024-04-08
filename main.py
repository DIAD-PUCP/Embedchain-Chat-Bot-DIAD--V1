# Basado en el diseño de chat de  CodingNepal - www.codingnepalweb.com
# Modificado y adaptado a partir de las sugerencias de David Morgan 

import os
import time

from embedchain import App

chat_with_doc_app = App()
chat_with_doc_app.add("document.pdf") # Cambiar por el nombre del archivo PDF que se desea consultar

# La clave de la API de OpenAI está en la variable de entorno OPENAI_API_KEY
# necesitamos establecerla para que el arreglo funcione

from flask import Flask, render_template, request

app = Flask(__name__,
            static_url_path="/",
            static_folder="static",
            template_folder="templates")

@app.route("/")
def home():
  return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
  try:
      question = request.json["question"]
      print("Received question:", question)
      question += "Responde a la consulta solo con referencia a los documentos que estás consultando. De no tener respuesta, por favor, indícalo."
      answer = chat_with_doc_app.query(question)
      print("Returned answer:", answer)
      return answer
  except Exception as e:
      print("Error:", str(e))
      return "Error processing request", 500


if __name__ == "__main__":
  app.run(host="0.0.0.0")
