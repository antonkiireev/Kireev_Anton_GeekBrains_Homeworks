a = 15 * 3
out = f'Результат a: {a:^15} Тип: {type(a)} Является дробным: {isinstance(a,float)}'
print(out)

b = 15 / 3
out = f'Результат b: {b:^15} Тип: {type(b)} Является строкой: {isinstance(b,str)}'
print(out)

c = 15 // 2
out = f'Результат c: {c:^15} Тип: {type(c)} Является списком: {isinstance(c,list)}'
print(out)

d = 15 ** 2
out = f'Результат d: {d:^15} Тип: {type(d)} Является списком: {isinstance(d,list)}'
print(out)