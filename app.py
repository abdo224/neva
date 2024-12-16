from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Bienvenue sur le serveur TCP/HTTP d'essai !"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
