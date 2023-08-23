# Faça um programa que peça um número inteiro e determine se ele 
# é ou não um número primo. Um número primo é aquele que é divisível 
# somente por ele mesmo e por 1.

num = int(input("Digite um número inteiro:\033[032m"))
contador = 0
print("\n\033[033mNúmeros Amarelos = São divisíveis")
print("\033[031mNúmeros Vermelhos = Não são divisíveis\n")
for i in range(1, num + 1):
    if num % i == 0:
        print('\033[33m', end='')
        contador +=1
    else:
        print('\033[31m', end='')
    print('{} '.format(i), end='')

if contador == 2:
    print(f'\n\033[mO número \033[032m{num}\033[m é primo, ou seja, divisível apenas por 1 ou {num}\033[m')
else:
    print(f'\n\033[mO número \033[032m{num}\033[m não é primo e pode ser divisível por \033[032m{contador}\033[m números')