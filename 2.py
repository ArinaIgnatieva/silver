a = []
b = []

n = int(input("Введите размер первого массива"))
m = int(input("Введите размер второго массива"))

result = []

for i in range (n):
    num = int(input("Введите элемент первого массива"))
    a.append(num)

for i in range (m):
    num = int(input("Введите элемент второго массива"))
    b.append(num)

for i in a:
    if i in b and i not in result:
        result.append(i)

print(a)
print(b)

print("Общие элементы первого и второго массивов:", result)