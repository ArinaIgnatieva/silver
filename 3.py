array = []

delta = int(input("Введите значение Delta"))

a = int(input("Введите размерность массива"))

for i in range (a):
    i = int(input("Введите элемент массива"))
    array.append(i)

min_el = min(array)

k = 0

for x in array:
    if x - min_el == delta:
        k += 1

print("Количество элементов, отличающихся отминимального на Delta:", k)