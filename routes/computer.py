import logging
from flask import Blueprint, request

computer = Blueprint('computer', __name__, url_prefix='/computer')

pokemon = []

logger = logging.getLogger(__name__)

@computer.route('/pokemon', methods=['GET'])
def get_pokemon():
    logger.info('Show Pokémon from computer')
    return pokemon, 200

@computer.route('/pokemon', methods=['POST'])
def add_pokemon():
    pokemon.append(request.json)
    logger.info('Add Pokémon to computer')
    return pokemon, 200

@computer.route('/pokemon/<int:id>', methods=['DELETE'])
def delete_pokemon(id):
    
    if id > len(pokemon):
        logger.error('Try to transfer Pokémon. Pokémon not found!')
        return 'Pokemon not found!', 404
    
    del pokemon[id]
    logger.info('Transfer Pokémon from computer')
    return pokemon, 200

@computer.route('/pokemon/<int:id>', methods=['PUT'])
def update_pokemon(id):
    
    if id > len(pokemon):
        logger.error('Try to update Pokémon. Pokémon not found!')
        return 'Pokémon not found!', 404
    
    pokemon[id] = request.json
    logger.info('Update Pokémon from computer')
    return pokemon, 200