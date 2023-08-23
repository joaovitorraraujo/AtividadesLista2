# Faça um programa, utilizando while, 
# que permita o usuário fazer contas de adição enquanto quiser.
print("Operação - \033[032mAdição!")
continuar = True
while continuar:
    num1 = int(input("\n\033[033mDigite um número:\033[m"))
    num2 = int(input("\033[033mDigite outro número:\033[m"))
    soma = num1 + num2
    print(f'\n{num1}\033[032m + \033[m{num2} = \033[032m{soma}\n')
    resposta = input("\033[033mDeseja realizar mais uma soma?[S ou N]\nResposta:\033[m")
    if resposta.lower()!= "s":
        continuar = False 