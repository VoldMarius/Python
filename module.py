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


def printing_matrix(values, num_rows, num_columns):
    matrix = [[i for i in range( num_rows)] for j in range(num_columns)]
    for i in range(num_rows):
        for j in range(num_columns):
            matrix[i][j] = values(i+1, j+1)
        
    for i in range(num_rows):
        for j in range(num_columns):
            print(f'{matrix[i][j]: 3}', end=' ')
        print()
