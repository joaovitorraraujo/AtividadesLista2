# Faça um programa que, dado um conjunto de N números, 
# determine o menor valor, o maior valor e a soma dosvalores

num1 = int(input("\033[033mDigite o primeiro número:\033[m"))
num2 = int(input("\033[033mDigite o segundo número:\033[m"))

if num1>num2:
    print(f'\nNúmero {num1},é \033[032mmaior')
    print(f'\033[mNúmero {num2},é \033[031mmenor')
elif num1 == num2:
    print("\n Os dois valores são \033[032miguais")
else:
    print(f'\nNúmero {num2},é \033[032mmaior')
    print(f'\033[mNúmero {num1},é \033[031mmenor')

soma = num1 + num2
print(f'\n\033[mSoma dos valores: \033[032m{num1}+{num2}={soma}\033[m')