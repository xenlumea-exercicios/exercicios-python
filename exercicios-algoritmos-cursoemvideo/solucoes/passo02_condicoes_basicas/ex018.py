# 18) Faça um programa que leia o ano de nascimento de uma pessoa,
# calcule a idade dela e depois mostre se ela pode ou não votar.

from datetime import date

ano_nascimento = int(input('Em qual ano você nasceu? '))

ano_atual = date.today().year
idade = ano_atual - ano_nascimento

mensagem = f'Com {idade} anos de idade, '

if idade < 16:
    mensagem += 'você não poderá votar nas eleições!'
else:
    mensagem += 'você poderá votar nas as eleições!'

print(mensagem)
