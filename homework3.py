def convert(n):
    if n < 7:
        return str(n)
    else:
        return convert(n // 7) + str(n % 7)

number = input("Введите целое простое десятичное число: ")

if number.isdigit():
    number = int(number)
    print(f"Семеричное представление: {convert(number)}")
else:
    print("Введите целое число.")