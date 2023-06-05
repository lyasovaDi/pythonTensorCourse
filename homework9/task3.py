# Дан файл test_file/task_3.txt можно считать, что это запись покупок в магазине, где указана только цена товара
# В каждой строке файла записана цена товара.
# Покупки (т.е. несколько подряд идущих цен) разделены пустой строкой
# Нужно найти сумму трёх самых дорогих покупок, которые запишутся в переменную three_most_expensive_purchases

# Здесь пишем код
def max_summ(array, count):
    our_sum = 0
    for i in range(count):
        buff = max(array)
        our_sum += buff
        array.remove(buff)
    return our_sum


file = open('test_file/task_3.txt', 'r')
mass1 = file.readlines()
mass2 = []
summ = 0
for line in mass1:
    if line != "\n":
        summ += int(line)
    else:
        mass2.append(summ)
        summ = 0

three_most_expensive_purchases = max_summ(mass2, 3)

assert three_most_expensive_purchases == 202346