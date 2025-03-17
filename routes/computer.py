import logging
from flask import Blueprint, request

computer = Blueprint('computer', __name__, url_prefix='/computer')

pokemon = []

logger = logging.getLogger(__name__)

@computer.route('/pokemon', methods=['GET'])
def get_pokemon():
    logger.info('Show pokemon from computer')
    return pokemon

@computer.route('/pokemon', methods=['POST'])
def add_pokemon():
    pokemon.append(request.json)
    logger.info('Add pokemon to computer')
    return pokemon

@computer.route('/pokemon/<int:id>', methods=['DELETE'])
def delete_pokemon(id):
    
    if id > len(pokemon):
        logger.error('Try to delete pokemon.Pokemon not found!')
        return 'Pokemon not found!'
    
    del pokemon[id]
    logger.info('Delete pokemon from computer')
    return pokemon

@computer.route('/pokemon/<int:id>', methods=['PUT'])
def update_pokemon(id):
    
    if id > len(pokemon):
        logger.error('Try to update pokemon.Pokemon not found!')
        return 'Pokemon not found!'
    
    pokemon[id] = request.json
    logger.info('Update pokemon from computer')
    return pokemon