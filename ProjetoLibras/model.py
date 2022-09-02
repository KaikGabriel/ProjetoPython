import mysql.connector
from conexao import conexao

class model:
    def __init__(self):
        self.resultado = 0
        self.db_connection = conexao()  # Abrindo a conexão com o banco de dados
        self.db_connection = self.db_connection.conectar()  # Método que realizar a conexão com o BD
        self.con = self.db_connection.cursor()  # Navegação no banco de dados

    def inserir(self, login, senha):
        try:
            sql = "insert into pessoa(codigo, login, senha) values('','{}','{}')".format(
                login, senha)
            self.con.execute(sql)
            self.db_connection.commit()  # Insere o dado no banco de dados
            return "{} linha afetada".format(self.con.rowcount)
        except Exception as erro:
            return erro

    def logar(self, login, senha):

        encontrar = "Select * from pessoa where login = '{}' and senha = '{}' ".format(login, senha)
        self.con.execute(encontrar)
        self.resultado = self.con.fetchall()
        if len(self.resultado) != 0:
            print('Logado com sucesso!')
            print(f'Bem Vindo {login}')
        else:
            print('Login ou Senha erradas!, Tente novamente')