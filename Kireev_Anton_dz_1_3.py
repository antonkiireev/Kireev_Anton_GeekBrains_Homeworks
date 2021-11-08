a = list(range(1,101,1))
for idx, item in enumerate(a, start=1):
    if item // 10 == 1:
        idx = 'процентов'
    elif item % 10 == 1:
        idx = 'процент'
    elif 2 <= item % 10 <= 4:
        idx = 'процента'
    elif 5 <= item % 10 <= 9:
        idx = 'процентов'
    elif item % 10 == 0:
        idx = 'процентов'
    print(item, idx)