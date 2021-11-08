amount = (int(input('Your amount of seconds = ')))    # первая версия
if amount < 60:
    print('0 days', '0 hours', '0 minutes', amount, 'sec')
elif 60 <= amount < 3600:
    print ('0 days', '0 hours', amount//60, 'minutes', amount%60,'sec')
elif 3600 <= amount < 86400:
    print ('0 days', amount//3600, 'hours', amount//60%60, 'minutes', amount%3600, 'sec')
elif 86400 <= amount:
    print (amount//86400, 'days', amount//3600%24,'hours', amount//60%60, 'minutes', amount%86400%3600%60, 'sec')
else:
    print('0')

# duration = int(input("Set your number of seconds: "))    # вторая версия
# days = duration // 86400
# if days >= 1:
#     print(days, 'days')
# else:
#     d = 0
# hours = (duration % 86400) // 3600
# if hours >= 1:
#     print(hours, 'hours')
# elif hours >= 24:
#     print(0, 'hours')
# else:
#     hours = 0
# minutes = ((duration % 86400) % 3600) // 60
# if minutes >= 1:
#     print(minutes, 'minutes')
# elif minutes >= 60:
#     print(0, 'minutes')
# else:
#     minutes = 0
# seconds = duration % 86400 % 3600 % 60 % 60
# if seconds >= 1:
#     print(seconds, 'seconds')
# elif seconds >= 60:
#     print(0, 'seconds')
# else:
#     seconds = 0