import requests


# Получение данных по полной дате

while True:
    user_date = input('Введите дату в формате "YYYY-MM-DD": ') # запрос даты у пользователя

    link = f'https://isdayoff.ru/{user_date}' # ссылка
    responce = requests.get(link).text # результат

    # Возможные результаты
    if responce == '0':            
        print('Рабочий день') # test_date: 2023-06-13
    elif responce == '1':          
        print('Нерабочий день') # test_date: 2023-06-12
    elif responce == '100':        
        print(f'Ошибка в дате: {user_date}') # test_date: 2023--16-1
    else:                          
        print('Данные не найдены') # test_date: 1000-01-23
    
    print('-' * 50)