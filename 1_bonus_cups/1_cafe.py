n = int(input())
file = open('1_bonus_cups/bonus_cups.txt', 'w')
file.write("Bonus cups: ")
file.write(str(n//6))
file.close()
