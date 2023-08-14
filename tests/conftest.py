"""
Conftest file
"""
import pytest

from common.api.trainer import TrainerApi
from common.helper.conf import Credential

@pytest.fixture(scope="session")
def api():
    """
    basic api fixture
    """
    pokemon_api = TrainerApi()
    yield pokemon_api

@pytest.fixture(scope="session")
def token():
    """
    Receive admin token 
    """
    yield Credential.trainer_token
