import ipaddress
import os
import json


class IP(object):
    def __init__(self, ip_list):
        self._ip_list = ip_list

    def get_ip(self):
        return self._ip_list

    def get_full_ip(self):
        full_list = []
        for ip in self._ip_list:
            ip = ipaddress.ip_address(ip).reverse_pointer
            full_list.append(ip[:-13])
        return full_list

    def get_ip_no_first_octet(self):
        full_list = []
        for ip in self._ip_list:
            ip = ip.split(".")
            ip.pop(0)
            ip_list = ".".join(ip)
            full_list.append(ip_list)
        return full_list

    def last_ip_octet(self):
        last_oct = []
        for ip in self._ip_list:
            ip = ip.split(".")
            last_oct.append(ip.pop(-1))
        return last_oct


c = IP(["172.20.250.4", "198.10.254.1", "192.16.254.3"])
print(c.get_ip())
print(c.get_full_ip())
print(c.get_ip_no_first_octet())
print(c.last_ip_octet())

# №2


class Json(object):
    def __init__(self, file1, file2=None, new=None):
        self._file1 = file1
        self._file2 = file2
        self._new = new

    def read_json(self):
        with open(self._file1, "r") as file:
            read = file.read()
            return read

    def write_json(self, text_to_add):
        with open(self._file1, "w") as file:
            json.dump(text_to_add, file, indent=4)

    def union_json(self):
        list_of_files = [self._file1, self._file2]
        with open(self._new, "w") as new:
            for file in list_of_files:
                with open(file, "r") as fi:
                    new.write(fi.read())

    def absolute_path(self):
        return os.path.abspath(self._file1)

    def relative_path(self):
        return os.path.relpath(self._file1)


data = {"user": []}
data["user"].append({
            "firstName": "John",
            "lastName": "Smith",
            "isAlive": True,
            "age": 27,
            "address": {
                "streetAddress": "21 2nd Street",
                "city": "New York",
                "state": "NY",
                "postalCode": "10021-3100"
            }})


f = Json("C:/Users/InnaDolina/PycharmProjects/StudyHillel/HomeWork#7/First.json")
print(f.read_json())

f = Json("C:/Users/InnaDolina/PycharmProjects/StudyHillel/HomeWork#7/Blank.json")
f.write_json(data)

f = Json("C:/Users/InnaDolina/PycharmProjects/StudyHillel/HomeWork#7/First.json",
         "C:/Users/InnaDolina/PycharmProjects/StudyHillel/HomeWork#7/Second.json",
         "C:/Users/InnaDolina/PycharmProjects/StudyHillel/HomeWork#7/new.json")
f.union_json()

f = Json("C:/Users/InnaDolina/PycharmProjects/StudyHillel/HomeWork#7/First.json")
print(f.relative_path())

f = Json("Second.json")
print(f.absolute_path())


# 3

class Unit(object):
    def __init__(self, unit_name, mac_address, ip_address, login, password):
        self._unit_name = unit_name
        self._mac_address = mac_address
        self._ip_address = ip_address
        self._login = login
        self._password = password

    @property
    def unit_name(self):
        return self._unit_name

    @unit_name.setter
    def unit_name(self, val):
        self._unit_name = val

    @property
    def mac_address(self):
        return self._mac_address

    @mac_address.setter
    def mac_address(self, val):
        self._mac_address = val

    @property
    def ip_address(self):
        return self._ip_address

    @ip_address.setter
    def ip_address(self, val):
        self._ip_address = val

    @property
    def login(self):
        return self._login

    @login.setter
    def login(self, val):
        self._login = val

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, val):
        self._password = val


x = Unit("switch", "00:E0:23:45:12:21", "172.20.250.4", "dataadmin", "123456")
print(x.unit_name)
print(x.mac_address)
print(x.ip_address)
print(x.login)
print(x.password)
x.unit_name = "wifi router"
print(x.unit_name)
x.password = "jgdfjbgjb"
print(x.password)
