numero = 0
dados = 0
soma = 0

numero = int(input('Digite mais um número para somar (digite 999 para parar): '))

while not numero == 999:

    soma += numero
    dados += 1
    numero = int(input('Digite mais um número para somar (digite 999 para parar): '))

print('Você digitou {} numeros e a soma foi {} '.format(dados, soma))