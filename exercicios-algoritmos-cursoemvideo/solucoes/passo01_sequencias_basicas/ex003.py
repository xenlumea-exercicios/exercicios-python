# 3) Crie um programa que leia o nome e o salário de um funcionário, mostrando uma mensagem no final.
# Ex: Nome do Funcionário: Maria do Carmo
# Salário: 1 850,45
# O funcionário Maria do Carmo tem um salário de R$1850,45 em junho.

nome_funcionario = input('Qual é o nome do funcionário? ')
salario = float(input('Quanto foi pago de salário ao funcionário este mês? '))

print(f'O funcionário {nome_funcionario} recebeu um salário de R$ {salario:.2f}.')
