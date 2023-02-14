def creat_list(n):  # создает лист из n элементов вводимых пользователем
    coll = list(
        map(int, input(f'Введите через пробел {n} элементов:  ').split()))

    if n > len(coll):
        return (f'Добавьте еще {n-len(coll)} элементов')
        creat_list(n)

    elif n < len(coll):
        coll = (coll[:n])

    return coll
def out_red(text):
    print("\033[31m {}" .format(text))
def out_yellow(text):
    print("\033[33m {}" .format(text))
def out_blue(text):
    print("\033[34m {}" .format(text))
