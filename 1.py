array = []

a = int(input("Введите размерность массива"))

for i in range (a):
    i = float(input("Введите элемент массива"))
    array.append(i)

max_el = max(array)

print("Максимальный элемент массива:", max_el)

next = array.index(max(array)) + 1

array[next:] = (len(array) - next) * [0]

print(array)