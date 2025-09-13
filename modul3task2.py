from random import sample

def get_numbers_ticket(min_value: int, max_value: int, quantity: int) -> list:

    try:
        # перевіряю основні обмеження:
        # min_value та max_value повинні бути в межах [1, 1000],
        # а quantity не може перевищувати довжину діапазону
        if min_value >= 1 and max_value <= 1000 and quantity <= (max_value - min_value + 1):
            print ("Your lottery numbers:")
            # повертаю відсортований список унікальних випадкових чисел
            return sorted(sample(range(min_value, max_value + 1), quantity))
        else:
            # якщо межі діапазону задані невірно → виводжу підказку
            if not (min_value >= 1 and max_value <= 1000):
                print ("Please enter a valid data value: min_value and max_value must be within [1, 1000], and min_value must be < max_value.")
            # якщо quantity виходить за допустимі межі → виводжу підказку
            elif not quantity <= (max_value - min_value + 1):
                print("Please enter a valid data value: quantity must be between 1 and the size of the range (max_value - min_value + 1).")
            # у будь-якому випадку повертаю порожній список, як вимагає завдання
            return []
    # перехоплюю помилки типів чи значень
    except (TypeError, ValueError):
        print("Please enter a valid data value: all parameters must be integers.")
        return []

# тестую функцію
print("коректні параметри")
print(get_numbers_ticket(1, 49, 6))

print("\nmin_value < 1")
print(get_numbers_ticket(0, 10, 5))

print("\nmax_value > 1000")
print(get_numbers_ticket(1, 2000, 10))

print("\nquantity > розмір діапазону")
print(get_numbers_ticket(1, 10, 20))

print("\nрядки замість чисел")
print(get_numbers_ticket("1", "10", "5"))

print("\nfloat замість int")
print(get_numbers_ticket(2.5, 600, 10))

