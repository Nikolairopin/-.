def Task1(n):
    # Использвуем остаток от делеения как признак нужной падежной формы
    if n % 10 == 1 and n % 100 != 11:
        return f"{n} компьютер"
    elif n % 10 in [2, 3, 4] and n % 100 not in [12, 13, 14]:
        return f"{n} компьютера"
    else:
        return f"{n} компьютеров"
