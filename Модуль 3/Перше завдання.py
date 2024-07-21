#Створіть функцію get_days_from_today(date), яка розраховує кількість днів між заданою датою і поточною датою.
#Вимоги до завдання:

#Функція приймає один параметр: date — рядок,
#що представляє дату у форматі 'РРРР-ММ-ДД' (наприклад, '2020-10-09').
#Функція повертає ціле число, яке вказує на кількість днів від заданої дати до поточної.
#Якщо задана дата пізніша за поточну, результат має бути від'ємним.
#У розрахунках необхідно враховувати лише дні, ігноруючи час (години, хвилини, секунди).
#Для роботи з датами слід використовувати модуль datetime Python.

from datetime import datetime

def get_days_from_today(date):
    try:
        input_date = datetime.strptime(date, "%Y-%m-%d")
        # Перетворення рядка дати у потрібний формат

        current_datetime = datetime.now()
        today = current_datetime.date()
        # Отримання поточної дати

        delta = today.toordinal() - input_date.toordinal()
        #Розрахунок різниці між сьогоднішньою і вказаною датою

        return delta
        # Повернення різниці у днях як ціле число
    except ValueError:
        return "Invalid date format. Please use 'YYYY-MM-DD'."
        # Обробка винятків для неправильного формату вхідних даних


date = input("Input your date in format 'YYYY-MM-DD': ")
print(get_days_from_today(date))