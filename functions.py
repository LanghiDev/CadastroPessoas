from datetime import datetime
from time import sleep


def escrever_arq(arq, txt):
    file = open(arq, 'a')
    file.write(txt)
    file.close()


def ver_arq(arq):
    file = open(arq, 'r')
    txt = file.read()
    pessoas = txt.split('\n')
    print('\033[1:30:47m'+('='*45).center(100))
    print('RELATÓRIO DE PESSOAS'.center(100), '\n' + ('='*45).center(100))
    sleep(1.5)
    dados_p = lambda pessoas: [p.split(',') for p in pessoas]
    pessoas = dados_p(pessoas)
    for p in range(0, len(pessoas)-1):
        print((f'{pessoas[p][0]:<27} \tIdade: {pessoas[p][1]}').center(100))
        reg = datetime.strptime(pessoas[p][2], '%Y-%m-%d %H:%M:%S')
        reg = reg.strftime('Data: %d/%m/%Y Horário: %Hh %Mmin %Sseg')
        print(f'\n\033[3:30:47m{reg.center(100)}')
        print(('-'*45).center(100))
    print(('='*45).center(100)+'                \033[m')
