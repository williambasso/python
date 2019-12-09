import MySQLdb

class PessoaDAO:
    def __init__(self):
        self.conn = MySQLdb.connect(host = 'mysql.topskills.study' ,database = 'topskills06' ,user = 'topskills06' ,passwd = 'William2019')
        self.cursor = self.conn.cursor()


    def listar(self):
        self.cursor.execute('select * from clientes')
        lista = self.cursor.fetchall()    
        return lista
    
    def listar_id(self,id):
        self.cursor.execute(f'select * from clientes where id = {id}')


    def buscar_por_id(self,id):
        self.cursor.execute(f'select * from clientes where id = {id}')
        item = self.cursor.fetchone()    
        return item

    def inserir(self, nome, sobrenome, cpf):
        self.cursor.execute(f'insert into clientes( nome, sobrenome, cpf ) values("{nome}" , "{sobrenome}" , {cpf})')
        self.conn.commit()

    def alterar(self, id, nome, sobrenome, cpf):
        self.cursor.execute(f'update clientes set nome = "{nome}" , sobrenome = "{sobrenome}", cpf = {cpf} where id = {id}')
        self.conn.commit()

    def deletar(self,id):
        self.cursor.execute(f'delete from clientes where id = {id}')
        self.conn.commit()

#inserir('Joao','Joao', 6456465)
#alterar(5,'Lucas','William',15115)
#deletar(4)
lista = PessoaDAO()

for l in lista.listar():
    print(l)



