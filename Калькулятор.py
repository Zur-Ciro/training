# Калькулятеринг
what = input( ' Что делаем? (+,-,**,/,*,%,//): ')
a = float(input( 'Введите первое число: ' ) ) #Float переводит целое число в дробное
b = float(input( 'Введите второе число: ' ) )

if what == '+' :
    c = a + b
    print('Ваш ответ: ' + str(c) )
elif what == '-':
    c = a - b
    print('Вот и он: ' + str(c) )
elif what == '**': #возведение в степень
    c = a ** b
    print('Готово: ' + str(c) )
elif what == '/': #деление
    c = a / b
    print ('Вуаля: ' + str(c) )
elif what == '*': #умножение
    c = a * b
    print ('Результат: ' + str(c) )
elif what == '%': #остаток при делении
    c = a % b
    print ('Вот ' + str(c))
elif what == '//': #целое число при делении (без остатка)
    c = a // b
    print ('Вот ' + str(c))

else:
    print('Выбирайте выражение, сэр. Этого нет в списке')
input()

