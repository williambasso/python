from funcmelhoradas import Acoes

terminal = ['piloto','chef','oficial1','oficial2','comissaria1','comissaria2','policial','bandido']
aviao = []


acoes = Acoes(terminal, aviao)

# IDA 1 
print(f'\033[1;32m--------------------------------------------------------------------------------\033[m')
acoes.iraviao(terminal[0],terminal[1])
print(f'\033[1;32m--------------------------------------------------------------------------------\033[m')

#VOLTA 1 
print(f'\033[1;32m--------------------------------------------------------------------------------\033[m')
acoes.irterminal(aviao[1])
print(f'\033[1;32m--------------------------------------------------------------------------------\033[m')
#IDA 2
acoes.iraviao(terminal[-1],terminal[0])
print(f'\033[1;32m--------------------------------------------------------------------------------\033[m')
#VOLTA2
acoes.irterminal(aviao[0])
print(f'\033[1;32m--------------------------------------------------------------------------------\033[m')
#IDA 3
acoes.iraviao(terminal[-1],terminal[0])
print(f'\033[1;32m--------------------------------------------------------------------------------\033[m')
#VOLTA 3
acoes.irterminal(aviao[0])
print(f'\033[1;32m--------------------------------------------------------------------------------\033[m')
#IDA 4
acoes.iraviao(terminal[-1],terminal[0])
print(f'\033[1;32m--------------------------------------------------------------------------------\033[m')
#VOLTA 4
acoes.irterminal(aviao[1])
print(f'\033[1;32m--------------------------------------------------------------------------------\033[m')
#ida5
acoes.iraviao(terminal[-1],terminal[0])
print(f'\033[1;32m--------------------------------------------------------------------------------\033[m')
#volta 5
acoes.irterminal(aviao[-1])
print(f'\033[1;32m--------------------------------------------------------------------------------\033[m')
#IDA 6
acoes.iraviao(terminal[0],terminal[1])
print(f'\033[1;32m--------------------------------------------------------------------------------\033[m')
#volta6
acoes.irterminal(aviao[2])
print(f'\033[1;32m--------------------------------------------------------------------------------\033[m')
#ida 7
acoes.iraviao(terminal[0],terminal[1])
print(f'\033[1;32m--------------------------------------------------------------------------------\033[m')
