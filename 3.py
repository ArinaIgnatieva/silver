array = []

delta = int(input("Введите значение Delta:"))

a = int(input("Введите размерность массива:"))

for i in range (a):
    i = int(input("Введите элемент массива:"))
    array.append(i)

min = array[0]
index = None

for i in range(a):
    if array[i] < min:
        min = array[i]
        index = i 

k = 0

for x in array:
    if x - min == delta:
        k += 1

print("Количество элементов, отличающихся от минимального на Delta:", k)