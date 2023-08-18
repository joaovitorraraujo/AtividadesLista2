# Faça um programa, utilizando while, 
# que permita o usuário fazer contas de adição enquanto quiser.
print("Operação - Adição!")
continuar = True
while continuar:
    num1 = int(input("\nDigite um número:"))
    num2 = int(input("Digite outro número:"))
    soma = num1 + num2
    print(f'\n{num1}+{num2}={soma}\n')
    resposta = input("Deseja realizar mais uma soma?[S ou N]\nResposta:")
    if resposta.lower()!= "s":
        continuar = False 