from src.hh_api import HhJobAPI


def interact_with_user():
    """
    Функция для взаимодействия с пользователем путем выполнения интерактивного поиска работы на hh.ru.
    Запрашивает у пользователя поисковый запрос, извлекает вакансии с помощью HhJobAPI,
    а затем позволяет пользователю просматривать и выполнять поиск по полученным вакансиям на основе зарплаты
    и ключевого слова. Никакие параметры или возвращаемые типы не упоминаются.
    """
    print("Добро пожаловать в интерактивный поиск вакансий в hh.ru!")
    api = HhJobAPI()
    search_query = input("Введите поисковый запрос для запроса вакансий из hh.ru: ")
    vacancies = api.get_vacancies({"text": search_query})

    if vacancies is not None:
        top_n = int(input("Введите количество вакансий для вывода топ N вакансий по зарплате: "))
        sorted_vacancies = sorted(vacancies, key=lambda v: v.get('salary', {}).get('from') or 0, reverse=True)
        print(f"Топ {top_n} вакансий по зарплате:")
        for vacancy in sorted_vacancies[:top_n]:
            print(vacancy['name'], vacancy.get('salary', {}).get('from', 'Зарплата не указана'))
    else:
        print("Не удалось получить вакансии. Попробуйте еще раз.")

    keyword = input("Введите ключевое слово для поиска вакансий: ")
    if vacancies is not None:
        keyword_vacancies = [v for v in vacancies if keyword.lower() in v.get('description', '').lower()]
        print(f"Вакансии с ключевым словом '{keyword}' в описании:")
        for vacancy in keyword_vacancies:
            print(vacancy['name'], vacancy.get('salary', {}).get('from', 'Зарплата не указана'))
    else:
        print("Не удалось получить вакансии для поиска ключевого слова.")

