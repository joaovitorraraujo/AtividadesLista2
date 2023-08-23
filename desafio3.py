# Altere o programa anterior para que ele aceite apenas números entre 0 e 1000
invalido = True
while invalido:
    print("\033[033mDIGITE APENAS VALORES DE 0 A 1000 E INTEIROS\n\033[m")
    num1 = int(input("\033[033mDigite o primeiro número:\033[m"))
    if num1 <0 or num1>1000:
        print("\n\033[031m===Digite um número válido!!!===\033[m\n")
    else:
        invalido = False
invalido = True
while invalido:       
    num2 = int(input("\033[033mDigite o segundo número:\033[m"))
    if num2 <0 or num2>1000:
        print("\n\033[031m===Digite um número válido!!!===\033[m\n")
    else:
        invalido = False
    

if num1>num2:
    print(f'\nNúmero {num1},é \033[032mmaior\033[m')
    print(f'Número {num2},é \033[031mmenor\033[m')
elif num1 == num2:
    print("\n Os dois valores são \033[032miguais\033[m")
else:
    print(f'\nNúmero {num2},\033[032mmaior\033[m')
    print(f'Número {num1},\033[031mmenor\033[m')

soma = num1 + num2
print(f'\nSoma dos valores: \033[032m{num1}+{num2}={soma}\033[m')