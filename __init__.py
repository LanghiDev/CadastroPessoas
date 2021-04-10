from datetime import datetime
from time import sleep
from functions import ver_arq, escrever_arq

while True:
    print('O QUE DESEJA FAZER?')
    print('[V] VER AS PESSOAS')
    print('[A] ADICIONAR PESSOA')
    try:
        resp = str(input('>>> ')).strip().lower()[0]
        if resp == 'v':
            print('\033[32mABRINDO ARQUIVO...\033[m')
            ver_arq('pessoas.txt')
            sleep(2)
        elif resp == 'a':
            try:
                while True:
                    nome = str(input('\033[3:33mNOME DA NOVA PESSOA: \033[m')).strip().title()
                    idade = str(input('\033[3:33mNOVA IDADE: \033[m'))
                    if nome == '' or any(c.isalpha() for c in idade) or any(l.isdigit() for l in nome):
                        print('\033[31m\nERRO: Valores Inválidos...\033[m\n')
                        sleep(1)
                    else:
                        break
            except:
                print('\033[31m\nAlgo deu errado! Voltando ao menu... \033[m\n')
            else:
                agrf = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
                agora = datetime.strptime(agrf, '%d/%m/%Y %H:%M:%S')
                print(f'\033[1:32mADICIONANDO NO ARQUIVO...\033[m')
                escrever_arq('pessoas.txt', f'{nome},{idade},{agora}')
                sleep(2)
                print(f'\033[1:34m\033[4:34m{nome.upper()}\033[m\033[1:34m ADICIONADO COM SUCESSO!')
                print(agora.strftime('%d/%m/%Y %H:%M:%S'), '\033[m\n')
                sleep(1)
        else:
            print('\n\033[31mPOR FAVOR, DIGITE APENAS "V" ou "A" SEM AS ASPAS...\033[m')
            sleep(2)
    except KeyboardInterrupt:
        print('\033[31m\nUsuário preferiu não informar os dados!\nEncerrando Programa... \033[m')
        print('\033[32mVOLTE SEMPRE!\033[m')
        break
    except:
        print('\033[31m\nAlgo deu errado! Tente novamente... \033[m')
