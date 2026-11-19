# Задание 1
i = 1
while i <= 10:
    print(i)
    i += 1

# Задание 2
total = 0
while True:
    num = int(input("Введите число (0 - выход): "))
    if num == 0:
        break
    total += num
print(total)

# Задание 3
n = int(input("Введите число: "))
count = 0
while n > 0:
    count += 1
    n //= 10
print(count)

# Задание 4
n = int(input("Введите число: "))
total = 0
while n > 0:
    total += n % 10
    n //= 10
print(total)

# Задание 5
n = int(input("Введите число: "))
result = ""
while n > 0:
    result += str(n % 10)
    n //= 10
print(result)

# Задание 6
n = int(input("Введите n: "))
power = 1
while power <= n:
    print(power)
    power *= 2

# Задание 7
password = "12345"
while input("Введите пароль: ") != password:
    print("Неверный пароль")
print("Доступ разрешён")

# Задание 8 
a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
while b != 0:
    a, b = b, a % b
print("НОД:", a)

# Задание 9
n = int(input("Введите n: "))
a, b = 0, 1
while a <= n:
    print(a, end=" ")
    a, b = b, a + b

# Задание 10
import random
secret = random.randint(1, 100)
attempts = 0
while True:
    guess = int(input("Ваш вариант: "))
    attempts += 1
    if guess < secret:
        print("Больше")
    elif guess > secret:
        print("Меньше")
    else:
        print("Угадал!")
        break
print("Количество попыток:", attempts)