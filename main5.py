'''Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. 
Поскольку разобраться в его кричалках не настолько просто, 
насколько легко он их придумывает, Вам стоит написать программу. 
Винни-Пух считает, что ритм есть, если число слогов (т.е. число гласных букв) 
в каждой фразе стихотворения одинаковое. Фраза может состоять из одного слова, 
если во фразе несколько слов, то они разделяются дефисами. 
Фразы отделяются друг от друга пробелами. Стихотворение  Винни-Пух вбивает 
в программу с клавиатуры. В ответе напишите “Парам пам-пам”, 
если с ритмом все в порядке и “Пам парам”, если с ритмом все не в порядке

*Пример:*

**Ввод:** пара-ра-рам рам-пам-папам па-ра-па-да    
    **Вывод:** Парам пам-пам  '''

'''res= input ( f'введите фразу: ' )
a= res.split()
f= lambda x:sum(map(x.count,'аоуыэеёиюя'))#lambda x: sum(1 for i in x if i in 'аоуыэеёиюя')#(lambda x:sum(map(x.count,'аоуыэеёиюя')))
tmp = f(a[0])
print (tmp)
if all(f(i) == tmp for i in a):
    print('Парам пам-пам')
else:
    print ('Пам парам')'''

'''Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6), 
которая принимает в качестве аргумента функцию, вычисляющую элемент по номеру 
строки и столбца. Аргументы num_rows и num_columns указывают число строк и 
столбцов таблицы, которые должны быть распечатаны. Нумерация строк и 
столбцов идет с единицы (подумайте, почему не с нуля). Примечание: бинарной 
операцией называется любая операция, у которой ровно два аргумента, как, 
например, у операции умножения.

*Пример:*

**Ввод:** `print_operation_table(lambda x, y: x * y) ` 
**Вывод:**'''

def print_operation_table(operation, num_rows=6, num_columns=6):
    a= [operation(i,j) for i in range(1, num_rows+1) for j in range(1, num_columns+1)]
    for i in a:
        print(a ) 
print_operation_table( lambda x, y: x * y )



          
