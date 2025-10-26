from flask import Flask, render_template, jsonify
import requests
import os

app = Flask(__name__)
NASA_API_KEY = os.getenv("NASA_API_KEY", "DEMO_KEY")  # use sua key ou DEMO_KEY

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/curiosidade')
def curiosidade():
    url = f'https://api.nasa.gov/planetary/apod?api_key={NASA_API_KEY}&count=1'
    response = requests.get(url).json()
    data = response[0]  # retorna uma lista, pegamos o primeiro item
    resultado = {
        "title": data.get("title", "Curiosidade Espacial"),
        "explanation": data.get("explanation", ""),
        "image": data.get("url", "")
    }
    return jsonify(resultado)

if __name__ == "__main__":
    print("Iniciando Flask...")  # só pra garantir que entra aqui
    app.run(debug=True)

