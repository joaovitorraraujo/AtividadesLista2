# Altere o programa anterior para que ele aceite apenas números entre 0 e 1000
invalido = True
while invalido:
    print("DIGITE APENAS VALORES DE 0 A 1000\n")
    num1 = int(input("Digite o primeiro número:"))
    if num1 <0 or num1>1000:
        print("\n===Digite um número válido!!!===\n")
    else:
        invalido = False
invalido = True
while invalido:       
    num2 = int(input("Digite o segundo número:"))
    if num2 <0 or num2>1000:
        print("\n===Digite um número válido!!!===\n")
    else:
        invalido = False
    

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