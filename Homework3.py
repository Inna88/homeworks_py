# task 1


def all_capitals(text):
    final = []
    for char in text:
        if char.istitle():
            final.append(char)
    res = "".join(final)
    print(res)


all_capitals("How are you? Eh, ok. Low or Lower? Ohhh.")