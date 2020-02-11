


mon_dict={1 : 'january' , 2 : 'february' , 3 : 'march', 3:'april', 5 : 'may', 6 : 'june', 7: 'july', 8:'august',9:'september', 10:'october', 11:'november', 12:'december'}

n_m = int(input('Введите номер месяца: '))
print(mon_dict[n_m])
if n_m < 3 or n_m == 12: #1 месяц - январь
    print('winter')
elif  n_m < 6:
    print('spring')
elif n_m < 9:
    print('summer')
elif n_m < 12:
    print('autmn')
