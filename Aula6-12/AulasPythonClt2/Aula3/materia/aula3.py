#---- 

# almocoDaEunice = {'carboidratos': ['batata'] , 'proteina': 'salmao' ,'salada': 'tomate', 'bebida':'corona', 'sobremesa': 'torta', 'molhos':['branco','mostarda'] }
# almocoDoYuri = {'carboidratos': ['batata-doce'] , 'proteina': 'frango-frito' ,'salada': None, 'bebida': 'agua', 'sobremesa': 'jacan' , 'molhos': ['madera','popeye'] }
# almocoDoAndrei = {'carboidratos': ['macarrao', '1kg de batata'] , 'proteina':'frango-inteiro' ,'salada': 'orta', 'bebida': 'guaraná-familia', 'sobremesa': 'torta-bolacha', 'molhos': ['madera','popeye'] }
# almocoDoAlfredo = {'carboidratos': ['picanha'] , 'proteina':'agua' ,'salada': 'salmao', 'bebida':'sorvete', 'sobremesa':'popeye' , 'molhos': ['corona','sukita']}



class Almoco:
    def __init__(self):        
       self.carboidratos = []
       self.proteina = ''
       self.salada = ''
       self.bebida = ''
       self.sobremesa = ''
       self.molhos = []

    def criar_prato(self):
        almoco =  f'Sala: {self.salada} Prot: {self.proteina}'
        return almoco

    def servir(self):
        pass

    def descartar(self):
        pass

    def imprimir_classe(self):
        print(self)

lista_almoco = []

almocoDaEunice = Almoco()
almocoDaEunice.salada = 'tomate'
almocoDoAlfredo = Almoco()
almocoDoAlfredo.salada = 'cebola'

lista_almoco.append(almocoDaEunice)
lista_almoco.append(almocoDoAlfredo)

lista_almoco[0].salada = 'alface'

# print(lista_almoco[0].salada)
# print(lista_almoco[1].salada)

print(almocoDaEunice)
print(lista_almoco[0])
almocoDaEunice.imprimir_classe()

