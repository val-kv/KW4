import requests


class JobAPI:
    def __init__(self, base_url):
        """
        Инициализирует объект с заданным значением base_url.
        :param base_url: str - Базовый URL-адрес объекта.
        :return: None
        """
        self.base_url = base_url

    def get_vacancies(self, params):
        """
        Отправляет запрос GET в API и возвращает список вакансий.
        :param params: Параметры, которые должны быть переданы в запросе.
        :return: Список вакансий.
        """
        response = requests.get(f"{self.base_url}/vacancies", params=params)
        if response.status_code == 200:
            return response.json()["items"]
        else:
            return None


class HhJobAPI(JobAPI):
    """
    Инициализирует новый экземпляр класса с указанным базовым URL-адресом.
    Parameters:
    base_url (str): Базовый URL-адрес для API.
    Returns:
        None
    """
    def __init__(self, base_url="https://api.hh.ru"):
        super().__init__(base_url)
