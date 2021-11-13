str_parts = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
idx = 0
while idx < len(str_parts):
    if str_parts[idx].isdigit():
        str_parts.insert(idx, '"')
        str_parts[idx + 1] = f'{int(str_parts[idx+1]):02}'
        str_parts.insert(idx + 2, '"')
        idx +=2
    elif str_parts[idx].startswith('+') and str_parts[idx][1:].isdigit():
        # долго ломал голову, такой метод не проходили, но решил применить
        str_parts.insert(idx, '"')
        str_parts[idx + 1] = f'{str_parts[idx + 1][0]}{int(str_parts[idx+1]):02}'
        str_parts.insert(idx + 2, '"')
        idx += 2
    idx += 1
final_result = ' '.join(str_parts)
print(final_result)

# с пробелами внутри кавычек не разобрался