# Задача-1
# Из текстового файла удалить все слова, содержащие от трех до пяти символов,
# но при этом из каждой строки должно быть удалено только четное количество таких слов.


def deletion_of_words(my_file):
    with open(my_file, "r") as file:
        strings = file.readlines()
    file.close()
    with open(my_file, "w") as file:
        for line in strings:
            line = line.split()
            if not line:
                continue
            delete = [w for w in line if 5 >= len(w) >= 3]
            if (len(delete) % 2) == 0:
                line = ""
            res = " ".join(line)
            file.write(res + "\n")
    file.close()


deletion_of_words("HW5.txt")

# Задача-2
# Текстовый файл содержит записи о телефонах и их владельцах.
# Переписать в другой файл телефоны тех владельцев, фамилии которых начинаются с букв К и С.


def new_contact_list(path1, path2):
    with open(path1, "r") as doc:
        my_dict = {}
        for line in doc:
            line = line.split()
            if not line:
                continue
            my_dict[line[0]] = line[1]
    doc.close()
    with open(path2, "w") as out:
        for k, v in my_dict.items():
            if k.startswith(("C", "K")):
                out.write(k + " ")
                out.write(v + "\n")
    out.close()


new_contact_list("New.txt", "Third.txt")
