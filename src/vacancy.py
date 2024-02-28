class Vacancy:
    """
    Инициализирует объект с предоставленным названием, ссылкой, зарплатой и описанием.
    Parameters:
        title (str): название вакансии.
        link (str): ссылка на вакансию.
        salary (float): зарплата в вакансии.
        description (str): описание вакансии.
    Returns:
        None
    """
    def __init__(self, title, link, salary, description):
        self.title = title
        self.link = link
        self.salary = self.validate_salary(salary)
        self.description = description

    @staticmethod
    def validate_salary(salary):
        """
        Проверяет указанную зарплату и возвращает ее, если она не пустая, в противном случае возвращает "Зарплата не указана".
        """
        if not salary:
            return "Зарплата не указана"
        else:
            return salary

    def compare_salary(self, other_vacancy):
        """
        Сравнивает зарплату между двумя вакансиями и возвращает результат в виде строкового сообщения.
         """
        if self.salary == "Зарплата не указана" or other_vacancy.salary == "Зарплата не указана":
            return "Сравнение невозможно из-за отсутствия информации о зарплате"
        self_salary = self.salary.replace(' ', '')
        other_salary = other_vacancy.salary.replace(' ', '')
        self_salary = self.extract_salary(self_salary)
        other_salary = self.extract_salary(other_salary)
        if self_salary < other_salary:
            return f"{self.title} имеет меньшую зарплату, чем {other_vacancy.title}"
        elif self_salary > other_salary:
            return f"{self.title} имеет большую зарплату, чем {other_vacancy.title}"
        else:
            return f"Зарплаты вакансий {self.title} и {other_vacancy.title} равны"

    @staticmethod
    def extract_salary(salary):
        """
        Извлекает среднюю заработную плату из заданного диапазона заработной платы или указанного значения заработной платы.
        :param salary: Входная строка заработной платы, подлежащая обработке.
        :return: Извлеченное значение средней заработной платы.
        """
        salary = salary.split('-')
        if len(salary) == 2:
            return (int(salary[0]) + int(salary[1])) / 2
        elif 'от' in salary[0]:
            return int(salary[0].replace('от', ''))
        elif 'до' in salary[0]:
            return int(salary[0].replace('до', ''))
        else:
            return int(salary[0].replace('до', ''))

