# Python: Flask test

This project runs with ``Python 3.10.12`` and Flask ``3.1.0``. 

## Description
This API it's a simple collection of Pokémon where you can add, delete and update Pokémon on your pokébag (where you can keep 6 Pokémon) and on your computer (where you can keep more Pokémon).

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
gunicorn -c gunicorn.conf.py app:app
```

## URL endpoints

| Method | URL | Description |
| ------ | --- | ----------- |
| GET | /pokebag/pokemon | Show Pokémon from pokebag |
| POST | /pokebag/pokemon | Add Pokémon to pokebag |
| DELETE | /pokebag/pokemon/<int:id> | Transfer Pokémon from pokebag |
| PUT | /pokebag/pokemon/<int:id> | Update Pokémon from pokebag |
| GET | /computer/pokemon | Show Pokémon from computer |
| POST | /computer/pokemon | Add Pokémon to computer |
| DELETE | /computer/pokemon/<int:id> | Transfer Pokémon from computer |
| PUT | /computer/pokemon/<int:id> | Update Pokémon from computer |
| GET | /view | Show all Pokémon in the collection |