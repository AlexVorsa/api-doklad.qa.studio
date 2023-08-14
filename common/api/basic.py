"""
Basic class for API
"""
import requests

from common.helper.logger import log

class Api:
    """Основной класс для работы с API"""
    _HEADERS = {'Content-Type': 'application/json'}
    _TIMEOUT = 10

    def __init__(self):
        """
        Initialization
        """
        self.response = None
        self.url = 'https://api.pokemonbattle.me:9104'

    def post(self, url: str, params: dict = None, json_body: dict = None, token: str = None):
        """
        Basic POST-request
        """
        if token:
            self._HEADERS['trainer_token'] = token

        self.response = requests.post(url=url,
                                      headers=self._HEADERS,
                                      params=params,
                                      json=json_body,
                                      timeout=self._TIMEOUT)
        log(response=self.response, request_body=json_body)
        return self

    def put(self, url: str, params: dict = None, json_body: dict = None, token: str = None):
        """
        Basic POST-request
        """
        if token:
            self._HEADERS['trainer_token'] = token

        self.response = requests.put(url=url,
                                     headers=self._HEADERS,
                                     params=params,
                                     json=json_body,
                                     timeout=self._TIMEOUT)
        log(response=self.response, request_body=json_body)
        return self


    def get(self, url: str, params: dict = None, token: str = None):
        """
        Basic GET-request
        """
        if token:
            self._HEADERS['trainer_token'] = token

        self.response = requests.get(url=url,
                                     params=params,
                                     headers=self._HEADERS,
                                     timeout=self._TIMEOUT)
        log(response=self.response)
        return self


    def delete(self, url: str, json_body: dict = None, token: str = None):
        """
        Basic DELETE-request
        """
        if token:
            self._HEADERS['trainer_token'] = token

        self.response = requests.delete(url=url,
                                        headers=self._HEADERS,
                                        json=json_body,
                                        timeout=self._TIMEOUT)
        log(response=self.response)
        return self

    def status_code_should_be(self, expected_code: int):
        """Проверяем статус-код ответа actual_code на соответствие expected_code"""
        actual_code = self.response.status_code
        assert expected_code == actual_code, f"\nОжидаемый результат: {expected_code} " \
                                             f"\nФактический результат: {actual_code}"
        return self
