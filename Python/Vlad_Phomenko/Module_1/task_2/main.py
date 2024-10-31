a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
n = 0
for i in range(1, 1000000):
    if a % i == 0 and b % i == 0:
        n = i
print("Наибольший общий делитель: ", n)