# print({i: i**3 for i in range(1, 11)})

# str_1 = 'pythonist'
# print({i: str_1.count(i) for i in str_1})

# print({i: i*i for i in range(1, int(input('Введите число ')) + 1)})

# dic = {'data1': 375, 'data2': 567, 'data3': -37, 'data4': 21}
# m = 1
#
# for i in dic.values():
#     m *= i
# print(m)

# Пол, Анна и Алекс писали
# контрольную. Пол и Анна
# получили 4, а умничка Алекс
# 5. Напишите программу,
# которая по имени
# показывает оценку. На вход
# программа получает имя.


# alco = {'whiskey': 50, 'beer': 5, 'wine': 30, 'vodka': 15}
# money = int(input('How much money do you have? '))
#
# for k, v in alco.items():
#     if money >= v:
#         print(k)

# Вы зашли пообедать в
# столовку. Программа получает
# на вход сколько денег у вас
# есть. И должна выводить
# сколько денег вы потратили и
# что вы поели.
menu = {'Борщ': 3, 'Салат': 2.25, 'Компот': 1.50, 'Сосиска в тесте': 2.15}
st_money = end_money = float(input())
list_1 = []
counter = 0

for k, v in menu.items():
    if end_money - v >= 0:
        end_money -= v
        list_1.append(k)

print(f'Купили {list_1}, потратили {st_money - end_money}')




# eat = [i for i in menu.keys()]
# sum = sum([i for i in menu.values()])
# print(sum)
#
# # oil = {'Январь': 3, 'Февраль': 3.15, 'Март': 3.20, 'Апрель': 3.35, 'Май': 3.75, 'Июнь': 3.10}
# max = 0
# month = ''
# for k, v in oil.items():
#     if v > max:
#         max = v
#         month = k
# print(f'{month} - месяц, в котором цена была наибольшей')


# Катя с Анной собрались
# поболтать о своем о
# женском. Какие посиделки
# без вина? Катя пьет красное,
# а Анна белое. Программа
# принимает на вход 2 числа:
# сколько бутылок выпила
# каждая. Выведи сколько
# денег они потратили.
# wine = {'red wine': 42, 'white wine': 37}
# katya_red = int(input('Сколько бутылок красного вина выбила Катя? '))
# anna_white = int(input('Сколько бутылок белого вина выбила Анна? '))
#
# print(f'Катя выпила красного вина на {wine["red wine"] * katya_red}\nАнна выбила белого вина на {wine["white wine"] * anna_white}')

# for i in range(len(wine)):
#     wine.popitem()
# print(wine)
#
# list_1 = []
# list_1.pop()