"""
Programa principal
Author: Vinicius Fernandes"
Version: 2025-04-03"
"""
import funcoes
from click import clear # importando somente a funcção 'clear'
clear() #limpa o console
funcoes.cabecalho("Bem vindo!",colunas=50)
funcoes.cabecalho("Olá turma, boa noite!",30)
funcoes.cabecalho()
funcoes.cabecalho(colunas=15)
print("fatorial de 5=",funcoes.fatorial(5))
print("fatorial de 5=",funcoes.fatorial_rec(5))

