
import os
import psutil
import time
import json
import xml.etree.ElementTree as elementTree
import zipfile as zf

def disks_info():
    d = psutil.disk_partitions()
    print('Информация о диске C:', d[0])
    print('Информация о диске D:', d[1])
    print('Получить поле диска:', d[0][0], d[1][0])
    print('Тип данных:', type(d), '\n')

    p = psutil.disk_usage(d[0][0])  # C диск
    print('Процент использования диска C: ', p)
    p = psutil.disk_usage(d[1][0])  # D disk
    print("D процент использования диска:", p)
    print('Тип данных»', type(p))

class File:
    def __init__(self, filename: str = ""):
        self.filename = filename
        if filename == "":
            self.filename = input("Введи имя нового файла\n") + ".txt"
            open(self.filename, "w")
            print("Файл", filename, "успешно создан")



    def write(self, text: str):
        open(self.filename, "w").write(text)
        print("Данные записаны")

    def printAll(self):
        print("Содержимое файла " + self.filename + ":")
        for line in open(self.filename, "r"):
            print(line)

    def delete(self):

        os.remove(self.filename)
        print("Файл " + self.filename + " удалён")




disks_info()

print("Создание файла:")
file = File("test.txt")

print("Добавление записей в файл")
file.write(input("Введи текст для записи в файл\n"))

time.sleep(2)
print("Вывод содержимого файла на экран")
file.printAll()

time.sleep(2)
print("Удаление файла")
file.delete()


post = input("Введи должность сотрудника\n")
name = input("Введи имя сотрудника\n")
age = int(input("Введи возраст сотрудника\n"))
sex = input("Введи пол сотрудника\n")

employee = {
    post: {
        "name": name,
        "age": age,
        "sex": sex
    }
}

with open("data_file.json", "w") as file:
    json.dump(employee, file)
    file.close()
    print("Данные записаны")

time.sleep(2)
print("Данные файла json:")
with open("data_file.json", "r") as read:
    data: dict = json.load(read)
    for i in data.values():
        print("name:", i["name"])
        print("age:", i["age"])
        print("sex:", i["sex"])

time.sleep(2)
print("Удаление файла")
File("data_file.json").delete()


print("Создание файла xml")
root = elementTree.Element("Employees")
e = elementTree.SubElement(root, post.capitalize(), {"name": name, "age": str(age), "sex": sex})
elementTree.ElementTree(root).write("employees.xml")

tree = elementTree.parse("employees.xml")
root = tree.getroot()

for child in root:
    print(child.tag, child.attrib)
os.remove("employees.xml")
print("Файл xml удален")

open("test.txt", "w").close()
z = zf.ZipFile("test.zip", "w")
z.write("test.txt")
z.close()

z1 = zf.ZipFile("test.zip", "r")
z1.printdir()
z1.close()
os.remove("test.zip")








