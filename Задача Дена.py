#Приветствие там и первая задача
t,f = 0,0 #t- True, f-False
print (' Доброго времени суток, добро пожаловать в ZurCorp ')
what = input(' Какой язык программирования мы изучаем? ')
what = what.lower()#переводит все в нижний регистр
if what == 'python':
    print ('Верно')
    t+= 1
elif what == 'питон':
    print ('Верно')
    t+=1
else:
    print ('Неверно')
    f+=1
what = input (' Ножик острый, кот лохматый, а арбуз ...? ')
what = what.lower()
if what == 'полосатый':
    print ('Верно')
    t+=1
else:
    print ('Неверно')
    f+=1
what = input ('Продолжите фразу "Я ослеп или ...?" ')
what = what.lower()
if what == 'нихуя':
    print ('Верно')
    t+=1
else:
    print ('Неверно')
    f+=1
what = input ('От нуля до талого по шкале? ')
if what == 'Баталова':
    print('Верно')
    t+=1
elif what == 'баталова':
    print('Верно')
    t+=1
else:
    print('Неверно')
    f+=1
what = input('Кто в детстве ходит на четырех ногах, в зрелости на двух, а в старости на трех? ')
what = what.lower()
if what == 'человек':
    print('Верно')
    t+=1
else:
    print('Неверно')
    f+=1
what = input ('Скайрим для... ')
what = what.lower()
if what == 'нордов':
    print('Верно')
    t+=1
else:
    print('Неверно')
    f+=1
print('\nВерно:{}\nНеверно{}'.format(t,f))
input()
