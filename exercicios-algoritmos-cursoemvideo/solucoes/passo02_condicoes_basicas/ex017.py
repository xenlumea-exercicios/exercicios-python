# 17) Escreva um programa que pergunte a velocidade de um carro.
# Caso ultrapasse 80Km/h, exiba uma mensagem dizendo que o usuário foi multado.
# Nesse caso, exiba o valor da multa, cobrando R$5 por cada Km acima da velocidade permitida.

velocidade_do_carro = float(input('Qual é a velocidade do carro em Km/h? '))

if velocidade_do_carro < 80:
    print('Você está dentro do limite de velocidade. Boa viagem!')
else:
    print('Você foi multado!')
