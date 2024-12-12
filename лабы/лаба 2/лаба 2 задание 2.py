# Титов Дмитрий Сергеевич, группа БВТ 2403
# Лабораторная №2 по ВвИТ, задание 2
def describe_person(name,age):
    if age == 'no':
        age = 30
    print('Имя:',name,'\nВозраст:',age)
    
name = input('Введите имя: ')
age = input('Введите возраст(опционально). При отказе введите no: ')
describe_person(name,age)