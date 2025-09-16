# імпортую клас datetime з модуля datetime
from datetime import datetime

def get_days_from_today(date: str):
    try:
        # при перетворенні рядка у об`єкт дати, я за допомогою методу replace()
        # видаляю усі пробіли (якщо вони є) на початку дати, в кінці дати або всередині дати
        # та за допомогою методу date() лишаю дату, прибираючи час
        date = datetime.strptime(date.replace(" ", ""), "%Y-%m-%d").date()
    except (ValueError, TypeError):
        # якщо дата у невірному форматі або дата некоректна, виводжу повідомлення і завершую
        print("Please enter a valid date in format 'YYYY-MM-DD'")
        return None
    # отримую сьогоднішню дату (без часу)
    date_now = datetime.today().date()
    # повертаю результат функції у вигляді обрахунку різниці у днях
    return (date_now - date).days

# тестую функцію з різними форматами введення дати
print("Коректна дата в минулому:")
print(get_days_from_today("2022-10-09"))

print("\nКоректна дата в майбутньому:")
print(get_days_from_today("2028-10-09"))

print("\nНекоректний формат (крапки замість дефісів):")
print(get_days_from_today("2024.04.22"))

print("\nНекоректний формат введення дати:")
print(get_days_from_today("2024-02-30"))

print("\nДата з зайвими пробілами:")
print(get_days_from_today(" 2024-04-22 "))

print("\nДата з зайвими пробілами у середині:")
print(get_days_from_today("2024 - 04 - 22"))
