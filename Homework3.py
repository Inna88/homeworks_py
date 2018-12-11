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
    var_2 = var_1*len(array)
    print("Multiplied previous result with the last element: ", var_2)


some_tuple((1, 5, 38, 0, 33, 6))


