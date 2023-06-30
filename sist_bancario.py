# sist_bancario
from IPython.utils.text import num_ini_spaces

menu = """

[d] Deposito
[s] Sacar
[e] extrato
[q] sair

=>"""

saldo = 0
limite = 500
extrato = ''
numero_saque = 0
limite_saque = 3

print(32 * '--')
print(10 * '-', 'BEM VINDO AO MENU DE SEUS SERVICOS BANCARIO', 9 * '-')
print(32 * '--', '\n')

while True:
    op = input(menu)
    if op == 'd':
        valor = float(input('Qual o valor deseja depositar?'))
        if valor > 0:
            saldo += valor
            extrato += f' Deposito: R$ {valor:.2f}'

        else:
            print('operacao falhou! O valor e invalido.')

    elif op == 's':
        valor = float(input('Qual valor deseja sacar'))
        execeu_saldo = valor > saldo
        execedeu_limite = valor > limite
        exedeu_limete = numero_saque >= limite_saque

        if execeu_saldo:
            print('operacao falhou! voce nao tem saldo suficiente')
        elif execedeu_limite:
            print('Operacao falhou! O valor de saque excede o limite.')
        elif valor > 0:
            saldo - +valor
            extrato += f'saque: R$ {valor:.2f}'
            numero_saque += 1
        else:
            print('opecao falhou! O valor informado e invalido')
    elif op == 'e':
        print(' \n', 5 * '=', 'Extrato', 5 * '=')
        print('Nao foram realizadas movimentacoes' if not extrato else extrato)
        print(15 * '=')
    elif op == 'q':
        break
    else:
        print('operacao invalida, por favor escolha uma das alternativas')
