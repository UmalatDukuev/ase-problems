count = 0

with open('3_pekar/client.txt', 'r', encoding='UTF-8') as file:
    lines = file.readlines()
    names_from_file = [line.strip() for line in lines[:3]]

def plushka(func):
    def wrapper(name, count):
        result = func(name, count)
        if count % 5 == 0:
            print("Вы получаете бесплатную плюшку!")
        return result
    return wrapper

@plushka
def Greeting(name, count):
    print("Привет, " + name + "!")

for name in names_from_file:
    count += 1
    Greeting(name, count)

for i in range(2):
    count += 1
    name = input()
    Greeting(name, count)

