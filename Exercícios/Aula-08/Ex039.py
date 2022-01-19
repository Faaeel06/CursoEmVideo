# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
# - Se ele ainda vai alistar ao serviço militar.
# - Se é a hora de se alistar.
# - se já passou do tempo do alistamento.
# Seu programa tabmém deverá mostrar o tempo que falta ou que passou do prazo.

import datetime
print(f'{"=" * 20:>}', 'PROGRAMA DE ALISTAMENTO MILITAR', f'{"=" * 20:>}')
data = datetime.date.today().year

data_nasc = int(input('Digite o ano do seu nascimento[com 4 dígitos]: '))

if (data_nasc + 18) == data:
    print('Está no seu ano de alistamento, procure uma junta do serviço militar de sua cidade.')
elif (data_nasc + 18) > data:
    print(f'Ainda não está no momento de alistar, ainda falta {((data - data_nasc) - 18) * -1} anos.')
else:
    print(f'Passaram {((data - data_nasc) - 18)} anos para o seu alistmaento.\n'
          f'Procure a junta de alistamento mais próxima e regualarize sua situação.')
