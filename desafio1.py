# A série de Fibonacci é formada pela sequência 0,1,1,2,3,5,8,13,21,34,55,... 
# Faça um programa que gere a série até que o valor seja maior que 500.

contador = 0
resultado = 0 
fibonacci = [0,1]

for contador in range(14):
    resultado = fibonacci[contador]+fibonacci[contador+1]
    fibonacci.append(resultado)
    contador+=1

    print(fibonacci)