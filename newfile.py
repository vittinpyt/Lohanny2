from flask import Flask, render_template
import os

app = Flask(__name__)
foto_dir = 'Armazenamentointerno/Pictures/FloresLohanny.jpg'

@app.route('/')
def index():
    fotos = [f for f in os.listdir(foto_dir) if f.endswith('.jpg')]
    return render_template('index.html', fotos=fotos)

if __name__ == '__main__':
    app.run(debug=True)
