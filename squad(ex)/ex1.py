# nicole PHP react MYSQL
# mateus python - Angular e Mongo
# tiago Java PostgreSQL vue
lista_nomes = ['Nicole', 'Mateus','Tiago']
nicole = ['php', 'react', 'mysql']
mateus = ['python', 'angular','mongodb']
tiago = ['java','vue', 'postgresql']
lista = []

while len(lista_nomes) > 0:
    for i in lista_nomes:
        print(f'\033[1;32m{i}\033[m')
    nome = input(f'\033[1;33mDigite o nome do funcionário para inserir na squad\033[m \n')
    print('\033[1;33mDigite o nome da  opção de banco de dados\033[m')
    print('\033[1;32m1 - Mysql 2 - PostgreSQL 3 - MongoDB\033[m')
    banco = input('')
    print('\033[1;36mDigite o nome da opção da linguagem\033[m')
    print('\033[1;35m - PHP 2 - Java 3 - Python\033[m')
    linguagem = input('')
    print('\033[1;36mDigite o nome da framework de front-end\033[m')
    print('\033[1;35m1 - React  2 - Angular 3 - Vue\033[m')
    framework = input('')
    lista.append(linguagem.lower())
    lista.append(framework.lower())
    lista.append(banco.lower())


    if nome.lower() == 'nicole':
        if lista[0] in nicole and lista[1] in nicole and lista[2] in nicole:
            print(f'\033[1;34mSe encaixa no squad\033[m')
            lista_nomes.remove('Nicole')
            
        else:
            print('\033[1;31mNão se encaixa no squad\033[m')
    elif nome.lower() == 'mateus':
        if lista[0] in mateus and lista[1] in mateus and lista[2] in mateus:
            print('\033[1;34mSe encaixa no squad\033[m')
            lista_nomes.remove('Mateus')
        else:
            print('\033[1;31mNão se encaixa no squad\033[m')
    elif nome.lower() == 'tiago':
        if lista[0] in tiago and lista[1] in tiago and lista[2] in tiago:
            print('\033[1;34mSe encaixa no squad\033[m')
            lista_nomes.remove('Tiago')
        else:
            print('\033[1;31mNão se encaixa no squad\033[m')

    lista = []
    if len(lista_nomes) == 0:
        print(f'\033[1;32mTodos os funcionários se encaixaram nas squads!\033[m')    

