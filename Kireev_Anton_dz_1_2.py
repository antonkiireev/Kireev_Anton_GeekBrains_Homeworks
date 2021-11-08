a = list(range(1, 1001, 2)) # без добавления 17-ти
for number in range(len(a)):
    a[number] **= 3
for cubes in range(len(a)):
    s = 0
    while a[cubes] > 0:
        digit = a[cubes] % 10
        s += digit
        a[cubes] //= 10
    if s % 7 == 0:
        a[cubes] = s
total = 0
for result in range(len(a)):
    if result > 0:
        total += result
print(total)

# a = list(range(1, 1001, 2)) # c добавлением 17
# for number in range(len(a)):
#     a[number] **= 3
# for plus in range(len(a)):
#     a[plus] += 17
# for cubes in range(len(a)):
#     s = 0
#     while a[cubes] > 0:
#         digit = a[cubes] % 10
#         s += digit
#         a[cubes] //= 10
#     if s % 7 ==0:
#         a[cubes] = s
# total = 0
# for result in range(len(a)):
#     if result > 0:
#         total += result
# print(total)