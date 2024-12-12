# Титов Дмитрий Сергеевич, группа БВТ 2403
# Лабораторная №2 по ВвИТ, задание 3
def is_prime(number):
    if number < 2:
        return False
    else:
        k = 0
        for i in range(2, number // 2 + 1):
            if number % i == 0:
                k = k + 1
                return False
    return True

number = int(input('Введите число '))
print(is_prime(number))
        
        