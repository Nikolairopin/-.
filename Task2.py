
def Task2(numbers):
    common_divisors = []
    # общий делитель не может быть больше наименьшего числа в массиве
    smallest_number = min(numbers)

    #перебераем все числа и ищем общий делитель
    for divisor in range(1, smallest_number + 1):
        if all(number % divisor == 0 for number in numbers):
            common_divisors.append(divisor)

    return common_divisors
