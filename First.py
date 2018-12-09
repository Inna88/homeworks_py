# task 1:

# Сгенерировать dict() из списка ключей ниже по формуле (key : key* key).
#  keys = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#  ожидаемый результат: {1: 1, 2: 4, 3: 9 …} 


def generate_dict():
    keys = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    my_dict = dict()
    for x in range(len(keys)):
        my_dict[keys[x]] = keys[x] * keys[x]
    print(my_dict)


generate_dict()


# task 2:
# generate a list() in range from 0 to 100 and save only even numbers into new list


def only_evens():
    my_list = list()
    for x in range(0, 101, 2):
        print(x)
    my_list = my_list.append(x)
    print(my_list)


only_evens()


# task 3: in random string replace all consonants with vowels


def replace_consonants():
    consonants = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm',
                  'n', 'p', 'q', 'r', 's', 't', 'v', 'x', 'w', 'z']
    vowels = ['a', 'e', 'i', 'o', 'u', 'y']
    print("Please enter your string")
    user_input = input().lower()
    import random
    for x in user_input:
        if any(x in consonants for x in user_input):
            result = random.choice(vowels)
            print(result)


replace_consonants()

# task 4
# 4)Дан массив чисел. [10, 11, 2, 3, 5, 8, 23, 11, 2, 5, 76, 43, 2, 32, 76, 3, 10, 0, 1]  
# 4.1) убрать из него повторяющиеся элементы 
# 4.2) вывести 3 наибольших числа из исходного массива  
# 4.3) вывести индекс минимального элемента массива
# 4.4) вывести исходный массив в обратном порядке 


def list_actions():
    my_list = [10, 11, 2, 3, 5, 8, 23, 11, 2, 5, 76, 43, 2, 32, 76, 3, 10, 0, 1]
    # 1) убрать из него повторяющиеся элементы 
    new_set = set(my_list)
    print("Removed duplicates:", new_set)
    # 2) вывести 3 наибольших числа из исходного массива
    new_list = list(new_set)
    new_list.sort()
    for x in new_list:
        max_three_nums = new_list[(len(new_list) - 3):]
    print("Max three numbers from the source array are: ", max_three_nums)
    # 3) вывести индекс минимального элемента массива
    print("Index of min element from the source array is: ", my_list.index(min(my_list)))
    # 4) вывести исходный массив в обратном порядке 
    my_list.reverse()
    print("The reverse order of the source array: ", my_list)


list_actions()


# tsk 5
# Найти общие ключи в двух словарях: 
# dict_one = { ‘a’: 1,  ‘b’: 2, ‘c’: 3,  ‘d’: 4 }
#   dict_two = { ‘a’: 6,  ‘b’: 7, ‘z’: 20,  ‘x’: 40 } 


def general_keys():
    d1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
    d2 = {'a': 6, 'b': 7, 'z': 20, 'x': 40}
    d1_to_set = set(d1.keys())
    d2_to_set = set(d2.keys())
    result_dict = d1_to_set.intersection(d2_to_set)
    print(result_dict)


general_keys()
