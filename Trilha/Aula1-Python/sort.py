numeros = input("").split()
numeros_int = []

for num in numeros:
    numeros_int.append(int(num))

tamanho_lista = len(numeros_int)

for i in range(tamanho_lista - 1):
    for j in range(tamanho_lista - 1):
        if numeros_int[j] > numeros_int[j + 1]:
            temp = numeros_int[j + 1]
            numeros_int[j + 1] = numeros_int[j]
            numeros_int[j] = temp


for i in range(tamanho_lista):
    print(numeros_int[i])
