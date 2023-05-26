import sqlite3

con = sqlite3.connect ('mercadinho.db')
cur = con.cursor()

cur.execute ('create table cliente\
    (cpf varchar (11) NOT NULL PRIMARY KEY,\
    nome varchar (64) NOT NULL,\
    email varchar (64) NOT NULL,\
    telefone varchar(20) NOT NULL,\
    endereco varchar (64) NOT NULL)')

cur.execute ('create table compra\
    (codigo integer NOT NULL PRIMARY KEY,\
    cpfcliente varchar (11),\
    data date NOT NULL,\
    meiopagamento int NOT NULL check (meiopagamento >= 1 and meiopagamento <=3))')

cur.execute ('create table produto\
    (codigo integer NOT NULL PRIMARY KEY,\
    nome varchar (64) NOT NULL,\
    categoria varchar (64) NOT NULL,\
    preco float NOT NULL,\
    qtdestoque integer NOT NULL check (qtdestoque >= 0),\
    desconto float NOT NULL check (desconto <=1 and desconto >= 0))')

cur.execute ('create table itemcompra\
    (codigo integer NOT NULL PRIMARY KEY,\
    codigocompra integer,\
    codigoproduto integer,\
    quantidade integer NOT NULL,\
    valor float NOT NULL, FOREIGN KEY (codigoproduto) REFERENCES produto(codigo) ON DELETE SET NULL)')









"""""""""
cur.execute ('drop table produto')
cur.execute ('drop table itemcompra')
cur.execute ('drop table compra')
cur.execute ('drop table cliente')
"""""""""


con.commit()
con.close()