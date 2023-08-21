print("Suas respostas serão validadas")
def validarnome(nome):
    return len(nome) > 3

validarsexo = 'fmFM'
validarestadocivil = 'scvdSCVD'

print("Digite um nome  maior que 3 caracteres!\n")
validacao = True
while validacao:
    nome = input("Seu nome:")
    if not validarnome(nome):
        print("\nDigite um nome válido\n")
    else:
        validacao = False

validacao = True
while validacao:
    idade = int(input("Sua idade:"))
    if idade<0 or idade >150:
        print("\nDigite uma idade entre 0 à 150 anos\n")
    else:
        validacao = False

validacao = True
while validacao:
    salario = int(input("Um salário:"))
    if salario<=0:
        print("\nDigite um salário maior que 0\n")
    else:
        validacao = False

validacao = True
while validacao:
    sexo = input("Seu sexo(F/M):")
    if sexo in validarsexo:
        validacao = False   
    else:
        print("\nDigite apenas 'F' ou 'M'\n")

validacao = True
while validacao:
    estadocivil = input("Seu estado civil(S/C/V/D):")
    if estadocivil in validarestadocivil:
        validacao = False   
    else:
        print("\nDigite apenas (S/C/V/D)\n")

print("\nDADOS REGISTRADOS E VALIDADOS!!!")

registro = input("Deseja ver o dados registrados?(S/N):")
match registro.lower():
    case "s":
        print(f'Nome: {nome}')
        print(f'Idade: {idade}')
        print(f'Salário: {salario}')
        print(f'Sexo: {sexo}')
        print(f'Estado Civil: {estadocivil}')
    case "n":
        print("Encerrando o programa!")
    case _:
        print("Encerrando o programa!")

   