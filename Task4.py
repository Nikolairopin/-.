def Task4(n):
    # для наглядности талицы нужно поставить между цифрами пробел
    # max_length расчитывает колво пробелов как колво символов в самом большом числе
    max_product = n * n
    max_length = len(str(max_product))

    header=[str(i).rjust(max_length) for i in range(1,n+1)]
    print(" "*(max_length+1)+" ".join(header))

    for i in range(1, n + 1):
        row = [str(i * j).rjust(max_length) for j in range(1, n + 1)]
        print(str(i).rjust(max_length) + " " + " ".join(row))
