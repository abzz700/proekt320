from proekt640Saidamir import count_vowels
from proekt640Abdulaziz import funk320FIO

print("Выберите чей код запускать:")
print("1 - Saidamir (подсчет гласных)")
print("2 - Abdulaziz (четность чисел)")

choice = input("Введите 1 или 2: ")

if choice == "1":
    text = input("Введите строку: ")
    print("Количество гласных:", count_vowels(text))

elif choice == "2":
    a = int(input("Введите первое число: "))
    b = int(input("Введите второе число: "))
    r1, r2 = funk320FIO(a, b)
    print("Первое число:", r1)
    print("Второе число:", r2)

else:
    print("Неверный выбор")