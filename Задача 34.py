# : Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. Поскольку
# разобраться в его кричалках не настолько просто, насколько легко он их придумывает, Вам
# стоит написать программу. Винни-Пух считает, что ритм есть, если число слогов (т.е. число
# гласных букв) в каждой фразе стихотворения одинаковое. Фраза может состоять из одного
# слова, если во фразе несколько слов, то они разделяются дефисами. Фразы отделяются друг
# от друга пробелами. Стихотворение Винни-Пух вбивает в программу с клавиатуры. В ответе
# напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, если с ритмом все не
# в порядке
# Ввод:                                                          Вывод:
# пара-ра-рам рам-пам-папам па-ра-па-дам                    Парам пам-пам
from module import out_blue, out_yellow
import os
os.system('cls')

string = 'пара-ра-рам рам-пам-папам па-ра-па-дам '
vowels = ['а', 'я', 'у', 'ю', 'и', 'ы', 'e', 'э']

out_blue((string.split()))


def looking_rhythm(parsed_string, sample):
    count = 0
    rhythm_count = []
    for i in range(len(parsed_string.split())):
        for j in range(len(parsed_string.split()[i])):
            for k in range(len(sample)):
                if vowels[k] in (parsed_string.split()[i])[j]:
                    count += 1
        rhythm_count.append(count)
        count = 0
    if all(x == rhythm_count[0] for x in rhythm_count):
        return ('Парам пам-пам')
    else:
        return ('Пам парам')


out_yellow(looking_rhythm(string, vowels))
