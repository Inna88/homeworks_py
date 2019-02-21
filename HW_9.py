# Задача-1
# Реализовать дескриптор валидации для аттрибута email.
# Ваш дескриптор должен проверять формат email который вы пытаетесь назначить
import re


class EmailDescriptor:
    def __init__(self, email=None):
        self.email = email

    def __get__(self, instance, owner):
        return instance.__dict__[self.email]

    def __set__(self, instance, value):
        instance._email = value
        if instance._email is None or "" == instance._email:
            raise ValueError("Empty input")
        match = re.match("^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$", instance._email)
        if match is None:
            raise ValueError("Invalid email")
        print("Valid email")


class MyClass:
    email = EmailDescriptor()


my_class = MyClass()
my_class.email = "validemail@gmail.com"

my_class.email = "skjfskf"


# Задача-2
# Реализовать синглтон метакласс(класс для создания классов синглтонов).

class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class MyClass(metaclass=Singleton):
    pass


c = MyClass()
b = MyClass()
assert id(c) == id(b)

