# Faça um programa que, dado um conjunto de N números, 
# determine o menor valor, o maior valor e a soma dosvalores

num1 = int(input("Digite o primeiro número:"))
num2 = int(input("Digite o segundo número:"))

if num1>num2:
    print(f'\nNúmero {num1},é maior')
    print(f'Número {num2},é menor')
elif num1 == num2:
    print("\n Os dois valores são iguais")
else:
    print(f'\nNúmero {num2},é maior')
    print(f'Número {num1},é menor')

soma = num1 + num2
print(f'\nSoma dos valores: {num1}+{num2}={soma}')