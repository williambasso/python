class Pessoa:
    def __init__(self, nome, sobrenome, cpf, id=None):
        self.id = id
        self.nome = nome
        self.sobrenome = sobrenome
        self.cpf = cpf