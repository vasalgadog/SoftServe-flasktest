import logging
from flask import Blueprint, request

pokebag = Blueprint('pokebag', __name__, url_prefix='/pokebag')

max_pokemon = 6

pokemon = []

logger = logging.getLogger(__name__)

@pokebag.route('/pokemon', methods=['GET'])
def get_pokemon():
    logger.info('Show pokemon from pokebag')
    return pokemon

@pokebag.route('/pokemon', methods=['POST'])
def add_pokemon():
    
    if len(pokemon) >= max_pokemon:
        logger.error('Try to add more than 6 pokemon')
        return 'You can\'t have more than 6 pokemon! You must to save on the computer'
    
    pokemon.append(request.json)
    logger.info('Add pokemon to pokebag')
    return pokemon

@pokebag.route('/pokemon/<int:id>', methods=['DELETE'])
def delete_pokemon(id):
    
    if id > len(pokemon):
        return 'Pokemon not found!'
    
    del pokemon[id]
    logger.info('Delete pokemon from pokebag')
    return pokemon

@pokebag.route('/pokemon/<int:id>', methods=['PUT'])
def update_pokemon(id):
    
    if id > len(pokemon):
        return 'Pokemon not found!'
    
    pokemon[id] = request.json
    logger.info('Update pokemon from pokebag')
    return pokemon