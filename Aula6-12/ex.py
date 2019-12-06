import MySQLdb

conn = MySQLdb.connect(host='mysql.topskills.study',
                       database='topskills06', user='topskills06', passwd='William2019')
cursor = conn.cursor()


def listar():
    cursor.execute('select * from local')
    lista = cursor.fetchall()
    return lista


def inserir(nome):
    cursor.execute(f'insert into values("{nome}")')
    conn.commit()


def alterar(id, nome):
    cursor.execute(f'update local set nome = "{nome}" where id = {id}')
    conn.commit()


def delete(id):
    cursor.execute(f'delete from local where id = {id}')
    conn.commit()




# inserir('')
#alterar(7,'nao tem café na sexta')
#delete(8)


for l in listar():
    print(l)