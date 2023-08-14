"""
Модуль для работы с тренерами
"""

from common.api.basic import Api


class TrainerApi(Api):
    """
    Methods for trainer
    """

    def get_trainer(self, trainer_id: int or str = None):
        """
        Get trainer. All or by trainer_id
        """
        return self.get(url=f'{self.url}/trainers', params={'trainer_id': trainer_id})

    def update_trainer(self, payload: dict, token: str):
        """
        Update trainer
        """
        return self.put(url=f'{self.url}/trainers', json_body=payload, token=token)

    def change_avatar(self, payload: dict, token: str):
        """
        Change avatar
        """
        return self.post(url=f'{self.url}/trainers/change_avatar', json_body=payload, token=token)

    def change_pass(self, payload: dict, token: str):
        """
        Update password for trainer
        """
        return self.put(url=f'{self.url}/trainers/re', json_body=payload, token=token)

    def registration(self, payload: dict):
        """
        Registration trainer
        """
        return self.post(url=f'{self.url}/trainers/reg', json_body=payload)

    def confirm_email(self, payload: dict):
        """
        Confirm email for trainer
        """
        return self.post(url=f'{self.url}/trainers/confirm_email', json_body=payload)

    def add_pokeball(self, pokemon_id: int, token: str):
        """
        Add pokemon to pokeball
        """
        payload = f"{'pokemon_id': '{pokemon_id}'}"
        return self.post(url=f'{self.url}/trainers/add_pokeball', json_body=payload, token=token)

    def delete_pokeball(self, pokemon_id: int, token: str):
        """
        Remove pokemon from pokeball
        """
        payload = f"{'pokemon_id': '{pokemon_id}'}"
        return self.put(url=f'{self.url}/trainers/delete_pokeball', json_body=payload, token=token)
