import time
from functools import wraps

# task 1


def unique_lines(file):
    lines = []
    for line in open(file):
        if line not in lines:
            lines.append(line)
    print(lines)
    yield lines


path = "HW10_file.txt"
x = unique_lines(path)
next(x)


# task 2


def coroutine(my_func):
    @wraps(my_func)
    def wrapper(*args, **kwargs):
        cor = my_func(*args, **kwargs)
        cor.next()
        return cor
    return wrapper


@coroutine
def grep(pattern, target):
    while True:
        line = (yield)
        if pattern in line:
            target.send(line)


@coroutine
def printer():
    while True:
        line = (yield)
        print(line)


@coroutine
def dispenser(targets):
    while True:
        item = (yield)
        for target in targets:
            target.send(item)


def follow(my_func_file, target):
    my_func_file.seek(0, 2)
    while True:
        line = my_func_file.readline()
        if not line:
            time.sleep(0.1)
            continue
        target.send(line)


file_open = open("log.txt")
follow(file_open,
       dispenser([
           grep("python", printer()),
           grep("is", printer()),
           grep("great", printer()),
       ])
       )
