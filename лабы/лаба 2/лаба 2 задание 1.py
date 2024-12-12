# Титов Дмитрий Сергеевич, группа БВТ 2403
# Лабораторная №2 по ВвИТ, задание 1
def greet(name):
    print('Здравствуйте,', name,'!')
    
def square(n):
    return n**2

def max_of_two(a,b):
    return max(a,b)

function_choice = input('Введите название функции, которую хотите запустить (greet,square,max_of_two): ')
if function_choice == 'greet':
    name = input('Ваше имя: ')
    greet(name)
elif function_choice == 'square':
    n = int(input('Введите число, квадрат которого необходимо найти: '))
    print('Квадрат числа = ',square(n))
elif function_choice == 'max_of_two':
    a = int(input('Введите 1 число: '))
    b = int(input('Введите 2 число: '))
    print('Максимальное из данных чисел =', max_of_two(a,b))
else:
    print('Функция не найдена!')
    
    