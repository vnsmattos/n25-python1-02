""" 
Código para demonstrar escopo de variáveis Python
Author: Vinicius Fernandes
Version: 2025-04-03
"""

from click import clear
#definindo um função
def calculo():
    a = 5
    b = a + c
    return b
#progrma principal
c = 10
clear()
print(calculo())

