nm= int(input('Введите номер месяца: '))
nm = nm - 1 #списки нумеруются с 0

mon_list=['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august''september', 'october', 'november', 'december', ]
namem = mon_list[nm]
#print(namem)
#print(mon_list.index(namem))


if mon_list.index(namem) < 3 or mon_list.index(namem) == 12: #1 месяц - январь
    print('winter')
elif  mon_list.index(namem) < 6:
    print('spring')
elif mon_list.index(namem) < 9:
    print('summer')
elif mon_list.index(namem) < 12:
    print('autmn')
