# Задание 1
grades = {"Анна": 5, "Иван": 4, "Мария": 5}
name = input("Введите имя ученика: ")
print(grades[name])

# Задание 2
my_dict = {"name": "Алиса", "age": 25}

my_dict["city"] = "Москва"
my_dict["age"] = 26

del my_dict["name"]
print(my_dict)

# Задание 3
my_dict = {"name": "Алиса", "age": 27}
key = input("Введите ключ: ")
print(my_dict.get(key, "Нет такого ключа"))

# Задани 4
my_dict = {"name": "Иван", "age": 22}
print("Ключи:", list(my_dict.keys()))
print("Значения:", list(my_dict.values()))
print("Количество пар:", len(my_dict))

# Задание 5
prices = {"хлеб": 50, "молоко": 80, "сыр": 300}
for item, price in prices.items():
    print(item, price)

# Задание 6
prices = {"хлеб": 50, "молоко": 80, "сыр": 300}
total = sum(prices.values())
most_expensive = max(prices, key=prices.get)
print("Сумма:", total)
print("Самый дорогой:", most_expensive)

# Задание 7
s = input("Введите строку: ")
char_count = {}
for char in s:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1
print(char_count)

# Задание 8
s = input("Введите слова через пробел: ")
words = s.split()
word_count = {}
for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1
print(word_count)
print("Самое частое:", max(word_count, key=word_count.get))

# Задание 9
my_dict = {"name": "Иван", "age": 20}
inverted_dict = {value: key for key, value in my_dict.items()}
print(inverted_dict)

# Задание 10
countries = ["Россия", "Франция", "Германия"]
capitals = ["Москва", "Париж", "Берлин"]
country_dict = dict(zip(countries, capitals))
country = input("Введите страну: ")
print(country_dict.get(country, "Нет такой страны"))