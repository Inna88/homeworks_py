# Task-1
# Создать объект менеджера контекста который будет переходить в папку которую он принимает на вход.
# Так же ваш объект должен принимать тип исключение которое он будет подавлять. Если флаг об исключении отсутствует,
# исключение должно быть поднято.

import os
from contextlib import contextmanager
from timeit import default_timer as timer


class TestContext(object):
    def __init__(self, Type_Error, path, flag):
        self._type_error = Type_Error
        self._flag = flag
        self._path = path

    def __enter__(self):
        try:
            os.chdir(self._path)
        except IOError:
            os.chdir(self._path)
        return self._path

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self._flag is False:
            raise self._type_error
        else:
            return True


with TestContext(FileNotFoundError, "C:/Users/InnaDolina/Desktop/HW_8_folder", False) as test:
    print(os.getcwd())

# Task-2
# Описать задачу выше но уже с использованием @contexmanager


@contextmanager
def open_folder(path):
    try:
        yield os.chdir(path)
    except FileNotFoundError:
        print("Error, file not found")


with open_folder("C:/Users/InnaDolina/Desktop/HW_8_folder") as new_folder:
    print(os.getcwd())

# Task-3
# Создать менеджер контекста который будет подсчитывать время выполняния блока инструкций


class TimeManager(object):
    def __init__(self):
        self._now = timer()

    def __enter__(self):
        self._after = timer()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        delta = self._after - self._now
        print("Execution time is: ", delta)


with TimeManager():
    a = [x for x in range(1000000)]





