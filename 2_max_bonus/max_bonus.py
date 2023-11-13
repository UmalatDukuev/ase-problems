with open('test_1.txt', 'r') as file:
    lines = file.readlines()
data = {}

for line in lines:
    name, number = line.strip().split()
    data[name] = int(number)

print(data)

max_name = max(data, key=data.get)
file = open('max_bonus.txt', 'w')
file.write("Max bonus goes to: ")
file.write(max_name)