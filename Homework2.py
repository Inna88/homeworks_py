# # task 1
# # 1.1) отсортировать массив из словарей по значению ключа ‘age' 
# # 1.2) сгруппировать данные по значению ключа 'city' 


def task1():
    data = [
        {'name': 'Viktor', 'city': 'Kiev', 'age': 30},
        {'name': 'Maksim', 'city': 'Dnepr', 'age': 20},
        {'name': 'Vladimir', 'city': 'Lviv', 'age': 32},
        {'name': 'Andrey', 'city': 'Kiev', 'age': 34},
        {'name': 'Artem', 'city': 'Dnepr', 'age': 50},
        {'name': 'Dmitriy', 'city': 'Lviv', 'age': 21}]
    from operator import itemgetter
    result = sorted(data, key=itemgetter('age'))
    print("1.1. Dictionaries are sorted by key 'age': ", result)
    import itertools
    sorted_data = sorted(data, key=itemgetter('city'))
    for key, group in itertools.groupby(sorted_data, key=lambda x: x['city']):
        print(key)
        print(list(group))


task1()


# # 2.  У вас есть последовательность строк. Необходимо определить наиболее часто встречающуюся строку в последовательности.


def most_frequent():
    list_var = ['a', 'a', 'bi', 'bi', 'Bi', 'abc', 'hgf', 'ABC', 'fty', 'abc', 'Abc']
    lower_list = [x.lower() for x in list_var]
    import collections
    import operator
    dict_var = collections.Counter(lower_list)
    print(max(dict_var.items(), key=operator.itemgetter(1))[0])


most_frequent()


# # 3.Дано целое число. Необходимо подсчитать произведение всех цифр в этом числе, за исключением нулей.


def multiply_numbers():
    num = 54307650
    num_str = str(num)
    my_list = [int(i) for i in list(num_str)]
    for x in my_list[1:]:
        result = my_list[0]
        for i in my_list[1:]:
            if i != 0:
                result = i * result
    print(result)


multiply_numbers()


# # task4 Есть массив с положительными числами и число n (def some_function(array, n)).
# # # Необходимо найти n-ую степень элемента в массиве с индексом n. Если n за границами массива, тогда вернуть -1.


def find_n_power_of_n_elem():
    array = [1, 6, 8, 0, 6, 9]
    n = 2
    if n < (len(array)-1):
        for index, x in enumerate(array):
            if index == n:
                res = x**n
                print(res)
    else:
        print("-1")


find_n_power_of_n_elem()


# 5) Есть строка со словами и числами, разделенными пробелами (один пробел между словами и/или числами).
# Слова состоят только из букв. Вам нужно проверить есть ли в исходной строке три слова подряд.
# Для примера, в строке "hello 1 one two three 15 world" есть три слова подряд.


def string_checker():
    my_str = "hello 1 one two three 15 world"
    count = 0
    for x in my_str.split(' '):
        if x.isalpha():
            count += 1
            if count == 3:
                return True
        else:
            count = 0
    return False


print(string_checker())
