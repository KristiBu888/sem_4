# Даны два неупорядоченных набора целых чисел (может быть, с повторениями). Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# На вход подается 2 числа через пробел: n m
# n - кол-во элементов первого множества.
# m - кол-во элементов второго множества.
# Затем подаются элементы каждого множества через пробел в виде строки. ! Писать input() не надо

# Пример
# На входе:
# var1 = '5 4' # количество элементов первого и второго множества
# var2 = '1 3 5 7 9' # элементы первого множества через пробел
# var3 = '2 3 4 5' # элементы второго множества через пробел
# На выходе:
# 3 5


# мое решение
var1 = '5 4'
var2 = '10 3 5 7 9'
var3 = '2 3 4 5'

s = var2 + " " + var3  # Объединяем все строки в одну
s = s.replace(' ', ',')  # Заменяем все пробелы на запятые

# Делим строку на массив отдельных чисел, указывая что числа между собой в строке разделены запятой.
# Если этого не сделать, то мы не сможем отдельно проверять числа, только символы в строке
s1 = s.split(',')

checked_nums_list = []
# Проверяем каждое ЧИСЛО (уже не символ) по отдельности и, если оно встречается больше 1 раза,
# и ранее не было првоерено, то записываем в массив checked_nums_list
for i in s1:
    if s.count(i) > 1 and i not in checked_nums_list:
        checked_nums_list.append(i)

print(' '.join(str(el) for el in checked_nums_list))


# решение 2
# mol = [int(x) for x in var1.split()]
# n = mol[0]
# m = mol[1]
# set_1 = set()
# set_2 = set()
# list_1 = list()
# a = [int(x) for x in var2.split()]
# k = set(a)
# for i in k:
#     set_1.add(i)
# b = [int(x) for x in var3.split()]
# k1 = set(b)
# for i in k1:
#     set_2.add(i)
# lok = set_1 & set_2
# kool = list(lok)
# kool.sort()
# for i in kool:
#     print(i, end=' ')
