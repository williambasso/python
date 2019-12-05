class Acoes:

    def __init__(self, terminal: list, aviao: list):
        self.terminal = terminal
        self.aviao = aviao

    def iraviao(self, p1, p2):
        self.terminal.remove(p1)
        self.terminal.remove(p2)
        print(f'TERMIAL -----CHEGANDO EM 5MINUTOS --------> AVIÃO \n'
              f'PILOTO {p1} PASSAGEIRO {p2}')
        self.aviao.append(p1)
        self.aviao.append(p2)
        print(f'Situação atual do terminal {self.terminal}')
        print(f'Situação atual do avião {self.aviao}')

    def irterminal(self, p1):
        self.aviao.remove(p1)
        self.terminal.append(p1)
        print(f'TERMINAL <-----5M---- PILOTO {p1}')
