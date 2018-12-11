# task 1


def all_capitals(text):
    final = []
    for char in text:
        if char.istitle():
            final.append(char)
    res = "".join(final)
    print(res)


all_capitals("How are you? Eh, ok. Low or Lower? Ohhh.")


# task 2


def some_tuple(array):
    var_1 = 0
    for x in array:
        if array.index(x) % 2 == 0:
            var_1 = var_1 + x
    print("Sum of even index elements is: ", var_1)
    var_2 = var_1 * len(array)
    print("Multiplied previous result with the last element: ", var_2)


some_tuple((1, 5, 38, 0, 33, 6))


# task 3
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
