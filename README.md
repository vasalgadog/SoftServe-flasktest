# Python: Flask test

This project runs with ``Python 3.10.12`` and Flask ``3.1.0``. 

## Description
This API it's a simple collection of pokemons where you can add, delete and update pokemon on your pokemon bag (where you can keep 6 pokemons) and on your computer (where you can keep more pokemons).

## Installation
Duplicate the ``.env.example`` file and rename it to ``.env``. Then, fill the variables with your values. Finally, run the following commands:

```bash
python -m venv .venv
source ./.venv/bin/activate
python -m pip install -r requirements.txt
```

## Usage

### Run the app

```bash
source .venv/bin/activate
python app.py
```

### Run the app with gunicorn

```bash
source .venv/bin/activate
export FLASK_APP=app.py
gunicorn -w 4 -b 0.0.0.0:5000 app:app
```

## URL endpoints

| Method | URL | Description |
| ------ | --- | ----------- |
| GET | /pokebag/pokemon | Show pokemon from pokebag |
| POST | /pokebag/pokemon | Add pokemon to pokebag |
| DELETE | /pokebag/pokemon/<int:id> | Delete pokemon from pokebag |
| PUT | /pokebag/pokemon/<int:id> | Update pokemon from pokebag |
| GET | /computer/pokemon | Show pokemon from computer |
| POST | /computer/pokemon | Add pokemon to computer |
| DELETE | /computer/pokemon/<int:id> | Delete pokemon from computer |
| PUT | /computer/pokemon/<int:id> | Update pokemon from computer |