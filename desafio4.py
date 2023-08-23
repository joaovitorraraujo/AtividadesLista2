print("\033[032mSUAS RESPOSTAS SERÃO VALIDADAS!\033[m\n")
def validarnome(nome):
    return len(nome) > 3

validarsexo = 'fmFM'
validarestadocivil = 'scvdSCVD'

print("Digite um nome  maior que 3 caracteres!")
validacao = True
while validacao:
    nome = input("\033[033mSeu nome:\033[m")
    if not validarnome(nome):
        print("\nDigite um nome válido\n")
    else:
        validacao = False

validacao = True
while validacao:
    idade = int(input("\033[033mSua idade:\033[m"))
    if idade<0 or idade >150:
        print("\nDigite uma idade entre 0 à 150 anos\n")
    else:
        validacao = False

validacao = True
while validacao:
    salario = int(input("\033[033mUm salário:\033[m"))
    if salario<=0:
        print("\nDigite um salário maior que 0\n")
    else:
        validacao = False

validacao = True
while validacao:
    sexo = input("\033[033mSeu sexo(F/M):\033[m")
    if sexo in validarsexo:
        validacao = False   
    else:
        print("\nDigite apenas 'F' ou 'M'\n")

validacao = True
while validacao:
    estadocivil = input("\033[033mSeu estado civil(S/C/V/D):\033[m")
    if estadocivil in validarestadocivil:
        validacao = False   
    else:
        print("\nDigite apenas (S/C/V/D)\n")

print("\n\033[032mDADOS REGISTRADOS E VALIDADOS COM SUCESSO!!!\n")

registro = input("Deseja ver o dados registrados?(S/N):\033[m")
match registro.lower():
    case "s":
        print(f'\033[033mNome: \033[m{nome}')
        print(f'\033[033mIdade: \033[m{idade} anos')
        print(f'\033[033mSalário: \033[mR${salario},00')
        print(f'\033[033mSexo: \033[m{sexo}')
        print(f'\033[033mEstado Civil: \033[m{estadocivil}')
        print("\n\033[031mEncerrando o programa!\033[m")
    case "n":
        print("Encerrando o programa!\033[m")
    case _:
        print("Encerrando o programa!\033[m")

   