while True:
    try:
        a = input("Введите первое число (или 'exit' для завершения): ")
        if a.lower() == 'exit':
            break
        b = input("Введите второе число (или 'exit' для завершения): ")
        if b.lower() == 'exit':
            break

        num1 = float(a)
        num2 = float(b)

        start = int(min(num1, num2)) + 1
        end = int(max(num1, num2))

        print(f"Целые числа между {num1} и {num2}:")
        for i in range(start, end):
            print(i, end=' ')
        print() 

    except ValueError:
        print("Ошибка! Введите корректные числа.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")
