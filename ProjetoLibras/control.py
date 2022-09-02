from model import model
import webbrowser as wb

class control:
    def __init__(self):
        self.opcao = -1
        self.modelo = model()
        self.resultado = 0

    def getOpcao(self):
        return self.opcao

    def setOpcao(self, opcao):
        self.opcao = opcao

    def menu(self):
        print('| Libras EAD |')
        print("Escolha uma das opções abaixo: \n" +
              "\n0. Sair" +
              "\n1. Aula 1" +
              "\n2. Aula 1.2" +
              "\n3. Aula 1.3" +
              "\n4. Playlist completa com as aulas" +
              "\n5. Site para sinais de libras relacionadas a internet e informática")
        self.setOpcao(int(input()))

    def menu2(self):
        print('| Login |')
        print('Escolha uma das opções abaixo: \n' +
              '\n0. Sair' +
              '\n1. Login' +
              '\n2. Cadastrar')
        self.setOpcao(int(input()))

    def operacoes1(self):
        while self.getOpcao() != 0:
            self.menu2()
            if self.getOpcao() == 0:
                print('Obrigado')
            elif self.getOpcao() == 1:
                print('Informe seu Login: ')
                login = input()
                print('Informe sua Senha: ')
                senha = input()
                self.modelo.logar(login, senha)
            elif self.cadastrar() == 2:
                self.cadastrar()
        else:
            print('Opção não é valida, tente novamente.')

    def operacoes(self):
        while self.getOpcao() != 0:
            self.menu()
            if self.getOpcao() == 0:
                print('Obrigado')
            elif self.getOpcao() == 1:
                wb.open('https://www.youtube.com/watch?v=IoRkuWWliFM')
            elif self.getOpcao() == 2:
                wb.open('https://www.youtube.com/watch?v=ZeSJQtD3rV0')
            elif self.getOpcao() == 3:
                wb.open('https://www.youtube.com/watch?v=vZkXAPsYkA0')
            elif self.getOpcao() == 4:
                wb.open('https://www.youtube.com/playlist?list=PLm7qw9oYBxanABvnJc4kWazFSv8uzK7PQ')
            elif self.getOpcao() == 5:
                wb.open('https://fesai.herokuapp.com/home')
            else:
                print('Opção não é valida, tente novamente.')

    def cadastrar(self):
        print('Informe seu nome de usuario: ')
        login = input()
        print('Informe sua senha: ')
        senha = input()
        print(self.modelo.inserir(login, senha))

