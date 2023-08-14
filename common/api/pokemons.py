"""
Модуль для работы с покемонами
"""

from common.api.basic import Api


class PokemonApi(Api):
    """
    Methods for pokemon
    """

    def create_pokemon(self, payload: dict, token: str):
        """
        Create pokemon
        """
        return self.post(url=f'{self.url}/pokemons', json_body=payload, token=token)

    def get_pokemon(self, params: dict = None):
        """
        Get pokemons
        """
        return self.get(url=f'{self.url}/pokemons', params=params)

    def kill_pokemon(self, pokemon_id: int, token: str):
        """
        Kill pokemon 
        """
        payload = f"{'pokemon_id': '{pokemon_id}'}"
        return self.post(url=f'{self.url}/pokemons/kill', json_body=payload, token=token)
