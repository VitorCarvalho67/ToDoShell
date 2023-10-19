from prisma import Prisma
from typing import Tuple
import os
import asyncio
import hashlib

# a class não pode ser async, mas os métodos sim além disso o __init__ não pode ser async e nem o __str__

class Pessoa:

    def __init__(self, name: str, email: str, password: str, db: Prisma) -> None:
        self.db = db
        self.name = name
        self.email = email
        self.password = password

    async def cadastrar(self) -> Tuple[str, str, str]:

        self.name = input('Digite seu nome: ')
        self.email = input('Digite um email: ')
        self.password = input('Digite uma senha: ')

        await self.srcCadastrar()

        return (self.name, self.email, self.password)

    async def srcCadastrar(self) -> bool:

        try:
            await self.db.connect()
            hash = hashlib.sha256(self.password.encode('utf-8')).hexdigest()

            await self.db.user.create({
                "name": self.name,
                "email": self.email,
                "password": hash
            })
            await self.db.disconnect()
            return True

        except Exception as e:
            print(e)
            return False

    async def login(self) -> None:
        self.email = input('Digite seu email: ')
        self.password = input('Digite sua senha: ')

        await self.srcLogin()

    async def srcLogin(self) -> bool:
        try:
            await self.db.connect()
            hash = hashlib.sha256(self.password.encode('utf-8')).hexdigest()
            user = await self.db.user.find_first(
                where={
                    "email": self.email,
                    "password": hash
                }
            )

            id = user.id

            await self.db.disconnect()
            if user:
                print('Logado com sucesso!')
                todo = Todo(self.db, id)
                await todo.run()

            else:
                print('Email ou senha incorretos!')
        except Exception as e:
            print(e)
            return False

    def limpar(self) -> None:
        os.system('cls' if os.name == 'nt' else 'clear')

    def __str__(self) -> str:
        return f'Nome: {self.name}\nEmail: {self.email}\nSenha: {self.password}'



# para executar o código async dentro de uma função normal, é necessário usar o asyncio.run(name_function())

class Main:

    def __init__(self) -> None:
        self.prisma = Prisma()
        self.pessoa = Pessoa('name', 'email', 'password', self.prisma)

    def menu(self) -> None:
        print('1 - Cadastrar')
        print('2 - Login')
        print('3 - Sair')

    def run(self) -> None:
        loop = asyncio.get_event_loop()
        while True:
            self.menu()
            op = input('Digite uma opção: ')
            if op == '1':
                self.limpar()
                print(loop.run_until_complete(self.pessoa.cadastrar()))
            elif op == '2':
                self.limpar()
                print(loop.run_until_complete(self.pessoa.login()))
            elif op == '3':
                break
            else:
                print('Opção inválida')
    def limpar(self) -> None:
        os.system('cls' if os.name == 'nt' else 'clear')

class Todo:
    def __init__(self, db: Prisma, id) -> None:
        self.id = id
        self.db = db
        print(self.id)

    def menu(self) -> None:
        print('1 - Cadastrar')
        print('2 - Deletar')
        print('3 - Listar')
        print('4 - Sair')

    async def run(self) -> None:
        self.limpar()
        loop = asyncio.get_event_loop()
        while True:
            self.menu()
            op = input('Digite uma opção: ')
            if op == '1':
                self.limpar()
                print(await self.cadastrar())  # Adicionado "await" aqui
            elif op == '2':
                self.limpar()
                print(await self.deletar(self.id))  # Adicionado "await" aqui
            elif op == '3':
                self.limpar()
                print(await self.listar())  # Adicionado "await" aqui
            elif op == '4':
                await self.sair()  # Adicionado "await" aqui
                break
            else:
                print('Opção inválida')

    async def cadastrar(self) -> None:
        try:
            await self.db.connect()
            title = str(input('Digite o título: '))
            description = str(input('Digite a descrição: '))

            await self.db.todo.create({
                "title": title,
                "description": description,
                "userId": self.id
            })
            await self.db.disconnect()
            print('Tarefa cadastrada com sucesso!')
        except Exception as e:
            print(e)

    async def deletar(self, id: str) -> None:
        idUser = id
        print(idUser)
        try:
            await self.db.connect()
            idTodo = str(input('Digite o id da tarefa: '))

            teste = await self.db.todo.find_first(
                where={
                    "id": idTodo,
                    "userId": idUser
                }
            )

            if not teste:
                print ('Tarefa não encontrada!')
            else:
                await self.db.todo.delete(
                    where={
                        "id": idTodo,
                    },
                )
                await self.db.disconnect()
                print('Tarefa deletada com sucesso!')

        except Exception as e:
            print(e)

    def limpar(self) -> None:
        os.system('cls' if os.name == 'nt' else 'clear')

    async def listar(self) -> None:
        try:
            await self.db.connect()
            todos = await self.db.todo.find_many(
                where={
                    "userId": self.id
                }
            )

            await self.db.disconnect()

            for todo in todos:
                titulo = " Título    | " + todo.title
                descricao = " Descrição | " + todo.description
                idddd = " Id        | " + todo.id

                lista = [titulo, descricao, idddd]

                maax = max(len(x) for x in lista)

                print("+" + "-" * 11 + "+" + "-" * ((maax + 2)-13) + "+")
                print("|" + lista[0] + " " * (maax - len(lista[0])) + " |")
                print("+" + "-" * 11 + "+" + "-" * ((maax + 2) - 13) + "+")
                print("|" + lista[1] + " " * (maax - len(lista[1])) + " |")
                print("+" + "-" * 11 + "+" + "-" * ((maax + 2) - 13) + "+")
                print("|" + lista[2] + " " * (maax - len(lista[2])) + " |")
                print("+" + "-" * 11 + "+" + "-" * ((maax + 2) - 13) + "+\n")

        except Exception as e:
            print(e)

    async def sair(self) -> None:
        await self.db.disconnect()
        print('Saindo...')
        exit()



if __name__ == '__main__':
    main = Main()
    main.run()