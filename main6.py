'''1.Открыть файл
2. Сохранить файл
3. Показать текст
4. Добавить контакт
5. Найти контакт
6. Изменить Контакт
6. Удалить Контакт
7. Выход'''

def open_file ():
    data = open ('phonebook.txt', 'a')
    data.close

def into_file ():
    data = open('phonebook.txt', 'a',encoding='UTF-8')
    with open  ('phonebook.txt', 'a',encoding='UTF-8') as data:
        new_contact= input( " Введите новый контакт: ")
        new_contact= new_contact + '\n'
        data.writelines(new_contact  )
into_file ()

def change_file():

    with open  ('phonebook.txt', 'r',encoding='UTF-8') as data:
        data=data.read()
        name2=(str(input ('Введите имя, которое хотите изменить: ')))
        new_name=str(input('Введите имя, на которое хотите поменять: '))
        new_data = data.replace(name2,new_name)
        with open ('phonebook.txt', 'w') as data:
            data.write(new_data)
    data.close  
change_file()
          



def reading_file():
    data= open('phonebook.txt', 'r')
    for line in data:
      print(line)
    data.close()
reading_file()



def faind_contact():
   with open ('phonebook.txt','r+',encoding='UTF-8') as into_file:
        data_list=[]
        name2= str(input( " Найти имя: "))
        for line in into_file:
            data_list.append(line.strip())
        print(data_list)
        for i in data_list:
            res = i.split()
            if res[0]== name2:
                print (i)
        print (' отсутствует данное имя ')
faind_contact()
      

def delete_contact():
   with open ('phonebook.txt','r',encoding='UTF-8') as data:
        data_list=[]
        name2= str(input( " удалить контакт: "))
        for line in data:
            data_list.append(line.strip())
        print(data_list) 
        data_list.remove(name2)
        print(' '.join(map(str, data_list))) 
        new_data =' '.join(map(str, data_list)) 
        with open ('phonebook.txt', 'w') as data:
            data.write(new_data)   
delete_contact()        
               