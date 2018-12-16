"""task 1: Дан произвольный текст.
Соберите все заглавные буквы в одно слово в том порядке как они встречаются в тексте."""


def all_capitals(text):
    final = [char for char in text if char.istitle()]
    res = "".join(final)
    print(res)


all_capitals("How are you? Eh, ok. Low or Lower? Ohhh.")


"""task2: Дан массив целых чисел. Нужно найти сумму элементов с четными индексами (0-й, 2-й, 4-й итд), 
затем перемножить эту сумму и последний элемент исходного массива."""


def some_tuple(array):
    var_1 = 0
    for x in array:
        if array.index(x) % 2 == 0:
            var_1 = var_1 + x
    print("Sum of even index elements is: ", var_1)
    var_2 = var_1 * len(array)
    print("Multiplied previous result with the last element: ", var_2)


some_tuple((1, 5, 38, 0, 33, 6))


"""task 3:
Дана строка и нужно найти ее первое слово.
При решении задачи обратите внимание на следующие моменты:
   1)В строке могут встречатся точки и запятые
   2)Строка может начинаться с буквы или, к примеру, с пробела или точки
   3)В слове может быть апостроф и он является частью слова
   4)Весь текст может быть представлен только одним словом и все"""


def replace_func(text):
    for ch in ["*", "_", "{", "}", "[", "]", "(", ")", ">",
               "<", "=", "#", "+", "-", ".", "!", "?", "$",
               "&", "%", "^", ":", ";", "@"]:
        text = text.replace(ch, " ")
    return text


def the_first_word_in_string(your_str):
    splited = replace_func(your_str).split()
    print(splited[0])


the_first_word_in_string("      ...!?@jffkfkfk jg !!! jhb * gjGGHDDD=jbjb")


"""task 4:
Изменить исходную строку на новую строку в которой первый и последний символы строки поменяны местами"""


def str_replace_first_with_last_sym(my_string):
    x = my_string.replace(my_string[-1], my_string[0])
    res = x.replace(x[0], my_string[-1], 1)
    print(res)


str_replace_first_with_last_sym("I love Odessa")


"""task 5: convert tuple() to string"""


def convert_tuple_to_str(my_tuple):
    print("".join(my_tuple))


convert_tuple_to_str(('e', 'x', 'e', 'r', 'c', 'i', 's', 'e', 's'))


"""task 6"""


def counter_digits(word):
    count_digits = 0
    for x in word:
        if x.isdigit():
            count_digits += 1
    return count_digits


def counter_letters(word):
    count_chars = 0
    for x in word:
        if x.isalpha():
            count_chars += 1
    return count_chars


def very_hard_func(given_str):
    array = given_str.split()
    new_list = []
    for word in array:
        if word.isalnum() is True and counter_letters(word) % 2 == 0 and counter_digits(word) % 2 == 1:
            new_list.append(word)
    print(new_list)
    print(max(new_list))


very_hard_func("test 5 a0A pass077 ?xy1 1234567cv")
