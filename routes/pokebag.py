import logging
from flask import Blueprint, request

pokebag = Blueprint('pokebag', __name__, url_prefix='/pokebag')

max_pokemon = 6

pokemon = []

logger = logging.getLogger(__name__)

@pokebag.route('/pokemon', methods=['GET'])
def get_pokemon():
    logger.info('Show Pokémon from pokebag')
    return pokemon, 200

@pokebag.route('/pokemon', methods=['POST'])
def add_pokemon():
    
    if len(pokemon) >= max_pokemon:
        logger.error('Try to add more than 6 Pokémon')
        return 'You can\'t have more than 6 Pokémon! You must to save on the computer', 401
    
    pokemon.append(request.json)
    logger.info('Pokémon captured and added to pokebag')
    return pokemon, 200

@pokebag.route('/pokemon/<int:id>', methods=['DELETE'])
def delete_pokemon(id):
    
    if id > len(pokemon):
        return 'Pokémon not found!', 404
    
    del pokemon[id]
    logger.info('Transfering Pokémon from pokebag')
    return pokemon, 200

@pokebag.route('/pokemon/<int:id>', methods=['PUT'])
def update_pokemon(id):
    
    if id > len(pokemon):
        return 'Pokémon not found!', 404
    
    pokemon[id] = request.json
    logger.info('Update Pokémon from pokebag')
    return pokemon, 200