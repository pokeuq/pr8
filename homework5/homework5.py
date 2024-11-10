def main():
    total_sum = 0.0 
    print("Введите числа для суммирования. Введите 'stop' или 'end' для завершения")
    
    while True:
        user_input = input("Введите число: ").strip()
        if user_input.lower() in ("stop", "end"):
            break
        try:
            number = float(user_input)
            total_sum += number
        except ValueError:
            print("Некорректный ввод! Пожалуйста, введите число или 'stop'/'end' для завершения")
    
    print(f"Сумма введенных чисел: {total_sum}")

if __name__ == "__main__":
    main()
