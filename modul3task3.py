import re

def normalize_phone(phone_number: str):
    # cпочатку прибираю всі символи, крім цифр і '+',
    # а також залишаю лише один '+' на початку
    correct_phone_number = re.sub(r"(?!^)\+", "", re.sub(r"[^\d+]", '', phone_number))
    # далі я починаю перебирати усі можливі варіанти, як було введено номер:
    # номер у форматі +380XXXXXXXXX (правильний міжнародний код України)
    if correct_phone_number.startswith("+380") and len(correct_phone_number) == 13:
        return f"{correct_phone_number}"
    # номер починається з 380 (але без '+')
    elif correct_phone_number.startswith("380") and len(correct_phone_number) == 12:
        return f"+{correct_phone_number}"
    # номер у скороченому форматі (0XXXXXXXXX)
    elif correct_phone_number.startswith("0") and len(correct_phone_number) == 10:
        return f"+38{correct_phone_number}"
    # номер у форматі +0XXXXXXXXX (помилковий варіант з '+')
    elif correct_phone_number.startswith("+0") and len(correct_phone_number) == 11:
        return f"+38{re.sub(r"^\+", '', correct_phone_number)}"
    # номер без початкового нуля і має лише 9 цифр(стаціонарний)
    elif not correct_phone_number.startswith("0") and len(correct_phone_number) == 9:
        return f"+380{correct_phone_number}"
    # у всіх інших випадках вважаю номер некоректним
    else:
        return None


raw_numbers = [
    "+067\\t123 +4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +++38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
    "+38065 789 67 5"
]

sanitized_numbers = [normalize_phone(phone_number) for phone_number in raw_numbers]
print("Нормалізовані номери телефонів для SMS-розсилки:")
for number in sanitized_numbers:
    print(number)

