# Задание 1
for i in range(1, 11):
    print(i)

# Задание 2
for i in range(2, 51, 2):
    print(i)

# Задание 3
for i in range(10, 0, -1):
    print(i)

# Заданеи 4
n = int(input("Введите n: "))
total = 0
for i in range(1, n + 1):
    total += i
print(total)

# Задание 5
n = int(input("Введите n: "))
factorial = 1
for i in range(1, n + 1):
    factorial *= i
print(factorial)

# Задание 6
n = int(input("Введите n: "))
for i in range(1, 11):
    print(f"{n} * {i} = {n * i}")

# Задание 7
numbers = [3, -1, 0, 5, -7, 8]
count = 0
for num in numbers:
    if num > 0:
        count += 1
print(count)

# Задание 8
s = input("Введите строку: ")
vowels = "аеёиоуыэюяАЕЁИОУЫЭЮЯ"
count = 0
for char in s:
    if char in vowels:
        count += 1
print(count)

# Задание 9
numbers = [3, 7, 2, 9, 5]
largest = numbers[0]
for num in numbers:
    if num > largest:
        largest = num
print(largest)

# Задание 10
for i in range(1, 10):
    for j in range(1, 10):
        print(f"{i * j:2}", end=" ")
