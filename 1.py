array = []

a = int(input("Введите размерность массива:"))

for i in range (a):
    i = float(input("Введите элемент массива:"))
    array.append(i)

max = array[0]
index = None 

for i in range(a):
    if array[i] > max:
        max = array[i]
        index = i 

for i in range(index + 1, a):
    array[i] = 0

print(array)