        
import sqlite3
from datetime import datetime

#CADASTRAR CLIENTE
def cadastrar_cliente ():
  con = sqlite3.connect ('mercadinho.db')
  cur = con.cursor()

  cpf = (input('Digite o CPF: '))
  nome = (input('Digite o nome: '))
  email = (input('Digite o email: '))
  telefone = (input('Digite o telefone: '))
  endereco = (input('Digite o endereço: '))

  cur.execute (f"insert into cliente VALUES\
    ('{cpf}', '{nome}','{email}', '{telefone}','{endereco}')")

  con.commit()
  con.close()
  print()
  print ('Usuário cadastrado com sucesso :)')

#REMOVER CLIENTE
def remover_cliente():
  con = sqlite3.connect ('mercadinho.db')
  cur = con.cursor()

  cpf = input('Digite o CPF: ')

  cur.execute (f"DELETE FROM cliente WHERE cpf = '{cpf}'")

  cur.execute (f"DELETE FROM compra WHERE cpfcliente = '{cpf}'")

  con.commit()
  con.close()
  print()
  print ('Usuário removido com sucesso :(')

#ATUALIZAR CLIENTE
def atualizar_cliente():
  con = sqlite3.connect ('mercadinho.db')
  cur = con.cursor()

  cpf = input('Digite o CPF do cliente cujo os dados serão alterados: ')
  nome = (input('Digite o nome: '))
  email = (input('Digite o email: '))
  telefone = (input('Digite o telefone: '))
  endereco = (input('Digite o endereço: '))

  cur.execute (f"UPDATE cliente SET nome ='{nome}', email ='{email}', telefone = '{telefone}', endereco = '{endereco}' WHERE CPF = '{cpf}'")
 
  con.commit()
  con.close()

  print()
  print ('Usuário alterado com sucesso :/')

#LISTAR CLIENTES
def listar_clientes():
  con = sqlite3.connect ('mercadinho.db')
  cur = con.cursor()

  result = cur.execute("SELECT * FROM cliente")  
  m= ["CPF", "Nome", "E-mail", "Telefone", "Endereço"]
  print (f"{m[0]:12}|{m[1]:30}|{m[2]:30}|{m[3]:21}|{m[4]:30}")
  print ('-'*120)
  for cliente in result:
      print (f"{cliente[0]:12}|{cliente[1]:30}|{cliente[2]:30}|{cliente[3]:21}|{cliente[4]:30}")
        
  con.commit()
  con.close()
  print()

#CADASTRAR PRODUTO
def cadastrar_produto():
  con = sqlite3.connect ('mercadinho.db')
  cur = con.cursor()

  nome = (input('Digite o nome: '))
  categoria = (input('Digite a categoria: '))
  preco = float(input('Digite o preço: '))
  qtdestoque = int(input('Digite a quantidade em estoque: '))
  while qtdestoque<0:
      print ('Informação inválida. Digite uma quantidade válida.')
      qtdestoque = int(input('Digite a quantidade em estoque: '))
  desconto = float(input('Digite o desconto: '))
  while desconto>1 or desconto<0:
      print ('Informação inválida. Digite um desconto válida.')
      desconto = float(input('Digite o desconto: '))

  cur.execute (f"insert into produto (nome, categoria, preco, qtdestoque, desconto)VALUES\
    ('{nome}', '{categoria}','{preco}', '{qtdestoque}','{desconto}')")

  con.commit()
  con.close()
  print()
  print ('Produto cadastrado com sucesso!')

#REMOVER PRODUTO
def remover_produto():
  con = sqlite3.connect ('mercadinho.db')
  cur = con.cursor()
  
  codigo = input('Digite o código do produto que deseja deletar: ')

  cur.execute (f"DELETE FROM produto WHERE codigo = '{codigo}'")

  con.commit()
  con.close()

  print()
  print ('Produto removido com sucesso.')

#ATUALIZAR PRODUTO
def atualizar_produto():
  con = sqlite3.connect ('mercadinho.db')
  cur = con.cursor()
  
  codigo=int(input('Digite o código do produto que deseja alterar: '))

  nome = (input('Digite o nome: '))
  categoria = (input('Digite a categoria: '))
  preco = float(input('Digite o preço: '))
  qtdestoque = int(input('Digite a quantidade em estoque: '))
  while qtdestoque<0:
      print ('Informação inválida. Digite uma quantidade válida.')
      qtdestoque = int(input('Digite a quantidade em estoque: '))
  desconto = float(input('Digite o desconto: '))
  while desconto>1 or desconto<0:
      print ('Informação inválida. Digite um desconto válida.')
      desconto = float(input('Digite o desconto: '))

  cur.execute (f"UPDATE produto SET nome ='{nome}', categoria ='{categoria}', preco = '{preco}', qtdestoque = '{qtdestoque}', desconto = '{desconto}' WHERE codigo = '{codigo}'")
 
  con.commit()
  con.close()
  print()
  print ('Produto alterado com sucesso.')

#LISTAR PRODUTOS
def listar_produtos():
  con = sqlite3.connect ('mercadinho.db')
  cur = con.cursor()

  result = cur.execute("SELECT * FROM produto")  
  m= ["Código", "Nome", "Categoria", "Preço", "Estoque", "Desconto"]
  print (f"{m[0]:6}|{m[1]:30}|{m[2]:30}|{m[3]:10}|{m[4]:10}|{m[5]:5}")
  print ('-'*100)
  for produto in result:
      print (f"{produto[0]:6}|{produto[1]:30}|{produto[2]:30}|{produto[3]:10}|{produto[4]:10}|{produto[5]:5}")
        
  con.commit()
  con.close()
  print()

#LISTAR PRODUTOS DE UMA CATEGORIA
def listar_categoria():
  con = sqlite3.connect ('mercadinho.db')
  cur = con.cursor()

  categoria = input("Digite o nome da categoria: ")
  result = cur.execute(f"SELECT * FROM produto WHERE categoria = '{categoria}'")
  result = cur.fetchall() 
  m= ["Código", "Nome", "Categoria", "Preço", "Estoque", "Desconto"]
  print (f"{m[0]:7}|{m[1]:30}|{m[2]:30}|{m[3]:10}|{m[4]:10}|{m[5]:5}")
  print ('-'*100)
  for result in result:
    print (f"{result[0]:7}|{result[1]:30}|{result[2]:30}|{result[3]:10}|{result[4]:10}|{result[5]:5}")

  con.commit()
  con.close()
  print()

#CADASTRAR COMPRA
def cadastrar_compra():
  con = sqlite3.connect ('mercadinho.db')
  cur = con.cursor()
  cpf= input('Digite o CPF do cliente: ')
  print("Meios de Pagamento\n [1] Crédito\n [2] Débito\n [3] Dinheiro")
  meiopagamento= int(input('Digite o número referente ao meio de pagamento: '))
  while meiopagamento != 1 and meiopagamento != 2 and meiopagamento !=3:
      print('Digite uma opção válida')  
      print("Meios de Pagamento\n [1] Crédito\n [2] Débito\n [3] Dinheiro")
      meiopagamento= int(input('Digite o número referente ao meio de pagamento: '))

  data = datetime.today().strftime ("%d-%m-%y")          
  cur.execute (f"insert into compra (cpfcliente, data, meiopagamento)VALUES\
      ('{cpf}','{data}','{meiopagamento}')")

  maximo = cur.execute("Select max(codigo) from compra ")
  maximo = cur.fetchone()

  print(f"O código da compra é: {(int(maximo[0]))}")
    
      
  con.commit()
  con.close()
  print()

#REMOVER COMPRA
def remover_compra():
  con = sqlite3.connect ('mercadinho.db')
  cur = con.cursor()

  codigo = input('Digite o código da compra que deseja deletar: ')

  cur.execute (f"DELETE FROM compra WHERE codigo = '{codigo}'")

  cur.execute (f"DELETE FROM itemcompra WHERE codigocompra = '{codigo}'")

  con.commit()
  con.close()
  print()

#ATUALIZAR COMPRA
def atualizar_compra():
  con = sqlite3.connect ('mercadinho.db')
  cur = con.cursor()

  codigo = input('Digite o código da compra que será alterada: ')
  cpfcliente = (input('Digite o CPF do cliente: '))
  data = datetime.today().strftime ("%d-%m-%y")
  meiopagamento = (input('Digite o meio de pagamento: '))
  print("Meios de Pagamento\n [1] Crédito\n [2] Débito\n [3] Dinheiro")
  while meiopagamento != 1 and meiopagamento != 2 and meiopagamento !=3:
    print('Digite uma opção válida')  
    print("Meios de Pagamento\n [1] Crédito\n [2] Débito\n [3] Dinheiro")  
    meiopagamento= int(input('Digite o número referente ao meio de pagamento: '))

  
  cur.execute (f"UPDATE cliente SET (cpfcliente ='{cpfcliente}', data = '{data}', meiopagamento = '{meiopagamento}' WHERE codigo = '{codigo}'")
 
  con.commit()
  con.close()
  print()
  
#LISTAR COMPRAS
def listar_compras():
  con = sqlite3.connect ('mercadinho.db')
  cur = con.cursor()

  result = cur.execute("SELECT * FROM compra")  
  m= ["Código", "CPF", "Data", "Meio de pagamento"]
  print("Meios de Pagamento  [1] Crédito  [2] Débito  [3] Dinheiro")
  print()
  print (f"{m[0]:10}|{m[1]:12}|{m[2]:10}|{m[3]:20}")
  print ('-'*55)

  for compra in result:
      print (f"{compra[0]:10}|{compra[1]:12}|{compra[2]:10}|{compra[3]:10}")
      
  con.commit()
  con.close()
  print()

#FUNÇÃO DE COMPRA
def item_compra():
  con = sqlite3.connect ('mercadinho.db')
  cur = con.cursor()

  codigo_compra = int(input('Digite o código da compra: '))
  while True:
      codigo_produto = int(input('Digite o código do produto: '))
      qtdatual = cur.execute(f"Select qtdestoque from produto WHERE codigo = {codigo_produto} ")
      qtdatual = cur.fetchone()

      quantidade = int(input('Digite a quantidade a ser vendida: '))
      while quantidade > (int(qtdatual[0])):
          print(f"Quantidade maior que estoque disponível. Temos em estoque apenas {(int(qtdatual[0]))} unidades. Insira outra quantidade")
          quantidade = int(input('Digite a quantidade a ser vendida: '))
      precound = cur.execute(f"SELECT preco FROM produto WHERE codigo = {codigo_produto} ")
      precound = cur.fetchone()
      desconto = cur.execute(f"SELECT desconto FROM produto WHERE codigo = {codigo_produto} ")
      desconto = cur.fetchone()
      precototal = quantidade * ((float(precound[0]))* (1 - (float(desconto[0]))))
      novaqdt = (int(qtdatual[0])) - quantidade

      cur.execute (f"insert into itemcompra (codigocompra, codigoproduto, quantidade, valor) VALUES\
          ('{codigo_compra}', '{codigo_produto}','{quantidade}', '{precototal}')")

      cur.execute (f"UPDATE produto SET (qtdestoque) ='{novaqdt}' WHERE codigo = '{codigo_produto}'")

      con.commit()
      print("Inserir mais itens à compra?\n [1] Sim\n [2] Não")
      decisao = int(input("Digite o número referente à opção desejada: "))
      while decisao != 1 and decisao != 2:
              print ("Digite uma opção válida")
              print("Inserir mais itens à compra?\n [1] Sim\n [2] Não")
              decisao = int(input("Digite o número referente à opção desejada: "))
      if decisao == 2:
          break

  con.close()
  print()
  print('Compra realizada com sucesso!')
    
#EXIBIR NOTA FISCAL
def nota_fiscal():
  con = sqlite3.connect ('mercadinho.db')
  cur = con.cursor()

  codigo = int (input('Digite o código da compra: '))
  print()
  print(" "*20,"Mercadinho do Seu Zé")
  print (" "*24,"CUPOM FISCAL")
  data = cur.execute (f"SELECT data from compra WHERE codigo = '{codigo}'")
  data = cur.fetchone()
  print (f"{' '*27}{data[0]}")
  print ('-'*65)

  produtos = cur.execute (f"SELECT codigoproduto, quantidade, produto.nome, produto.preco, valor FROM produto \
  INNER JOIN itemcompra ON codigoproduto = produto.codigo \
  WHERE codigocompra = '{codigo}'")

  produtos = cur.fetchall()

  m= ["Cod.Prod.", "Qtd.", "      Produto", " Vl.Unt(R$)", " Vl.Item(R$)"]
  print (f"{m[0]:10}|{m[1]:5}|{m[2]:20}|{m[3]:12}|{m[4]:12}")
  print ('-'*65)

  for tupla in produtos:
      print (f"{(tupla[0]):5}     {(tupla[1]):3}x   {(tupla[2]):20} {(tupla[3]):7}  {(tupla[4]):12}")
  print ('-'*65)

  total = cur.execute (f"SELECT sum(valor) FROM itemcompra WHERE codigocompra = {codigo}")
  total = cur.fetchone()
  for result in total:
      print (f'TOTAL(R$): {(total[0]):48}')
  print()

#EXIBIR RELATÓRIO DO NÚMERO DE PRODUTOS E USUÁRIOS CADASTRADOS, ALÉM DO NÚMERO DE COMPRAS O RELATÓRIO DEVE EXIBIR UM TOTAL DE TODAS AS COMPRAS REALIZADAS (VALOR BRUTO)
def relatorio ():
  con = sqlite3.connect ('mercadinho.db')
  cur = con.cursor()
  result = cur.execute("SELECT sum(qtdestoque) from produto")
  result = cur.fetchone()

  result1 = cur.execute("SELECT count(cpf) from cliente")
  result1 = cur.fetchone()

  result2 = cur.execute("SELECT count(codigo) from compra")
  result2 = cur.fetchone()

  result3 = cur.execute("SELECT sum(valor) from itemcompra")
  result3 = cur.fetchone()

  print (' '*26,'TOTAL')
  print ('-'*65)
  m= ["Produtos", "Clientes", "Compras", "Vendas"]
  print (f"{m[0]:15}|{m[1]:15}|{m[2]:15}|{m[3]:15}")
  print ('-'*65)

  print(f"{result[0]:15}|{result1[0]:15}|{result2[0]:15}|{result3[0]:15}")
        
  con.close()
  print()

#MENU
def menu():
  while True:
    print("Escolha uma das opções abaixo:\n\
    [1] Cadastrar\n\
    [2] Alterar\n\
    [3] Listar\n\
    [4] Deletar\n\
    [5] Realizar compra\n\
    [6] Relatório\n\
    [7] Nota Fiscal\n\
    [0] Encerrar Menu")

    opcao = int(input("Digite o número referente à opção desejada: "))

    if opcao == 1:
        print ("O que você deseja cadastrar?\n [1] Cliente\n [2] Produto")
        opcao_cadastro = int(input("Digite o número referente à opção desejada: "))
        while opcao_cadastro != 1 and opcao_cadastro != 2:
          print ("Digite uma opção válida.")
          opcao_cadastro = int(input("Digite o número referente à opção desejada: "))
        if opcao_cadastro == 1:
            cadastrar_cliente()
        elif opcao_cadastro == 2:
            cadastrar_produto()
        

    elif opcao == 2:
        print ("O que você deseja alterar?\n [1] Cliente\n [2] Produto")
        opcao_alteracao = int(input("Digite o número referente à opção desejada: "))
        while opcao_alteracao != 1 and opcao_alteracao != 2:
          print ("Digite uma opção válida.")
          opcao_alteracao = int(input("Digite o número referente à opção desejada: "))
        if opcao_alteracao == 1:
            atualizar_cliente()
        elif opcao_alteracao == 2:
            atualizar_produto()
        


    elif opcao == 3:
        print ("O que você deseja listar?\n [1] Cliente\n [2] Produto\n [3] Compra")
        opcao_listar = int(input("Digite o número referente à opção desejada: "))
        while opcao_listar != 1 and opcao_listar != 2 and opcao_listar != 3:
          print ("Digite uma opção válida.")
          opcao_listar = int(input("Digite o número referente à opção desejada: "))
        if opcao_listar == 1:
            listar_clientes()
        elif opcao_listar == 2:
            print("Deseja listar por categoria?\n [1] Sim\n [2] Não")
            categoria = int(input("Digite o número referente à opção desejada: "))
            while categoria != 1 and categoria != 2:
              print ("Digite uma opção válida")
              print("Deseja listar por categoria?\n [1] Sim\n [2] Não")
              categoria = int(input("Digite o número referente à opção desejada: "))
            if categoria == 1:
              listar_categoria()
            elif categoria == 2:
              listar_produtos()
        elif opcao_listar == 3:
            listar_compras()

    elif opcao == 4:
        print ("O que você deseja Deletar?\n [1] Cliente\n [2] Produto\n [3] Compra")
        opcao_deletar = int(input("Digite o número referente à opção desejada: "))
        while opcao_deletar != 1 and opcao_deletar != 2 and opcao_deletar != 3:
          print ("Digite uma opção válida.")
          opcao_deletar = int(input("Digite o número referente à opção desejada: "))
        if opcao_deletar == 1:
            remover_cliente()
        elif opcao_deletar == 2:
            remover_produto()
        elif opcao_deletar == 3:
            remover_compra()
  
    elif opcao == 5:
        print ("Digite as informações abaixo.")
        cadastrar_compra()
        print ("Insira os produtos que deseja comprar.")
        item_compra()

    elif opcao == 6:
      relatorio ()

    elif opcao == 7:
      nota_fiscal()

    elif opcao == 0:
      break

    else:
      print("Digite uma opção válida.")


menu()
