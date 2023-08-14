"""
Модуль для проведения битв
"""

from common.api.basic import Api


class BattleApi(Api):
    """
    Methods for battle
    """

    def summon_to_battle(self, attack_id: int, defend_id: int, token: str):
        """
        Summon an enemy Pokemon to battle
        """
        payload = {"attacking_pokemon": f"{attack_id}", "defending_pokemon": f"{defend_id}"}
        return self.post(url=f'{self.url}/battle', json_body=payload, token=token)

    def get_battle(self, trainer_id: int):
        """
        Get battle
        """
        return self.get(url=f'{self.url}/battle', params={'trainer_id': f'{trainer_id}'})
