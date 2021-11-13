rubles = int(input('Сколько рублей: '))    # захотелось создать список через ввод данных
coins = int(input('Сколько копеек: ')) / 100
items = int(input('Сколько товаров: '))
price_start = rubles + coins
idx = 0
set_items = [0]

import random

while idx < items:  # в данной области решил поработать с рандомными числами, доизучил
    set_items.append(round((price_start * random.randint(3, 9)),2))
    idx +=1
print(set_items)


# for goods in set_items:    # part A
#     rub_items = int(goods)
#     coins_items = (goods - rub_items) * 100
#     print(f'{rub_items} руб {coins_items:02.0f} коп')


# print(id(set_items))         # part B
# set_items.sort()
# print(id(set_items))
# for item in set_items:
#     rub_items = int(item)
#     coins_items = (item - rub_items) * 100
#     print(f'{rub_items} руб {coins_items:02.0f} коп', end=',')
#
#
# for good_item in sorted(set_items)[::-1]:    # part C
#     rub_items = int(good_item)
#     coins_items = (good_item - rub_items) * 100
#     print(f'{rub_items} руб {coins_items:02.0f} коп', end=',')
#
for good_item in sorted(set_items)[::-1][:5]:    # part D
    rub_items = int(good_item)
    coins_items = (good_item - rub_items) * 100
    print(f'{rub_items} руб {coins_items:02.0f} коп', end=',')