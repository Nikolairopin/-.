def Task3(n1, n2):
    #используем вспомогательную функцию IsPrime для нахождения простого числа
    def IsPrime(n):
        if n <= 1:
            return False
        elif n <= 3:
            return True
        elif n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True
    # используем генератор списка для более лаконичного решения
    return [num for num in range(n1, n2 + 1) if IsPrime(num)]
