while True:
    try:
        a = input("Введите первое целое число (или 'exit' для выхода): ")
        if a.lower() == 'exit':
            break
        b = input("Введите второе целое число (или 'exit' для выхода):  ")
        if b.lower() == 'exit':
            break
        # Преобразуем введенные данные в целые числа
        num1 = int(a)
        num2 = int(b)
        
        # Выводим сумму
        print(f"Сумма первого числа: {num1} и второго числа: {num2} равна: {num1 + num2}")
    
    except ValueError:
    
        print("Ошибка! Введите корректные целые числа")
    except Exception as e:
        # Обработка других возможных исключений
        print(f"Произошла ошибка: {e}")
