"""
Pokemonbattle.
Test project.
"""
import pytest

from faker import Faker
from pytest_voluptuous import S
from common.helper.schema.trainer import valid_trainer, error_trainer, update_trainer


class TestTrainers():
    """
    Tests for trainers
    """
    CASE_TRAINERS = [
        {'id': 1927, 'status_code': 200, 'schema': valid_trainer},
        {'id': -1927, 'status_code': 400, 'schema': error_trainer},
        {'id': 'qwerty', 'status_code': 404, 'schema': error_trainer},
        {'id': '$#', 'status_code': 404, 'schema': error_trainer}
    ]

    @pytest.mark.parametrize('case', CASE_TRAINERS)
    def test_get_trainer(self, case, api):
        """
        Get trainers
        """
        response = api.get_trainer(trainer_id=case['id'])

        api.status_code_should_be(case['status_code'])

        if response.response.status_code in [400, 404]:
            assert S(case['schema']) == response.response.json()
            assert response.response.json()['message'] == "Тренер отсутствует", ''
        else:
            assert S(case['schema']) == response.response.json()

    def test_update_trainer(self, api, token):
        """
        Get trainers
        """
        fake = Faker()
        Faker.seed(0)
        payload = {"name": f"{fake.name_nonbinary()}", "city": "Tokyo"}
        response = api.update_trainer(payload=payload, token=token)

        api.status_code_should_be(200)
        assert S(update_trainer) == response.response.json()
        assert response.response.json()['message'] == "Информация о тренере обновлена", ''
    