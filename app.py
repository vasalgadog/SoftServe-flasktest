from flask import Flask
from dotenv import load_dotenv
from routes import computer, pokebag
import os
import logging

load_dotenv()

HOST=os.environ.get('HOST')
PORT=os.environ.get('PORT')
DEBUG=os.environ.get('DEBUG')

app = Flask(__name__)

app.register_blueprint(pokebag.pokebag)
app.register_blueprint(computer.computer)

logging.basicConfig(filename='myapp.log', level=logging.INFO)

@app.route('/', methods=['GET'])
def index():
    return 'My Pokémon collection!'

@app.route('/view', methods=['GET'])
def get_pokemon():
    all_pokemon = {
                    "pokebag" : pokebag.get_pokemon(),
                   "computer" : computer.get_pokemon()
                }
    return all_pokemon

if __name__ == '__main__':
    app.run(host=HOST, port=PORT, debug=DEBUG)