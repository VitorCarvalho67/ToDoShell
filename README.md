<div align="center">
  <img src="https://github.com/VitorCarvalho67/ToDoShell/assets/102667323/e2bf9cc2-4ded-40cf-9f7d-3676cf15de60" />
</div>

# ToDoShell
This Python project is a robust and feature-rich ToDoList application, built entirely using object-oriented programming and employing asynchronous techniques. It harnesses the capabilities of MySQL, Python, Prisma, and Poetry to provide users with a seamless task management system. Users can easily register, log in, and once logged in, they have the flexibility to create new tasks, complete with titles and descriptions. From the main menu, users can efficiently list all their tasks, add new ones, remove existing tasks, and log out. This project showcases the power of object-oriented design and async programming, combining Python for the backend, MySQL for data storage, Prisma for database management, and Poetry for dependency management, ensuring a responsive and user-friendly experience.

## How to use:

1. **Clone o Repositório:**

   ```
   git clone https://github.com/VitorCarvalho67/ToDoShell.git
   ```

2. **Navegue até a Pasta do Projeto:**

   ```
   cd ToDoShell
   ```

3. **Instale as Dependências com Poetry ou Rode o venv diretamente**

   Use o seguinte comando para instalar as dependências listadas no arquivo `pyproject.toml`:

   ```
   poetry install
   ```

   ou

   ```
   python -m venv venv
   # Windows
   .\venv\Scripts\activate.bat
   # Linux e *nix
   . ./venv/bin/activate
   # Instalar dependências
   pip install -r requirements.txt
   ```

3-1 **(Opcional) Subir o banco de dados com docker-compose**
Docker precisa estar instalado na sua máquina

```
docker-compose up -d
```

4. **Migre o banco prisma**
   Você precisa migrar o banco prisma para as tabelas serem criadas

   ```
   prisma db push
   ```

5. **Execute o Projeto:**

   Execute o seu projeto Python com Poetry. Substitua `main.py` pelo nome do arquivo principal do seu projeto:

   ```
   poetry shell
   python main.py
   ```

   ou

   ```
   # Dentro do venv
   (venv) $ python main.py
   ```

Isso iniciará seu projeto.


![Screenshot_207](https://github.com/VitorCarvalho67/ToDoShell/assets/102667323/bed71059-e10a-40bc-8214-4f4f356d25c0)

Certifique-se de que as configurações do Prisma e as variáveis de ambiente estejam devidamente configuradas em seu projeto, como especificado na documentação do Prisma. Este guia simples deve ajudá-lo a configurar e executar seu projeto com o Prisma como dependência usando Poetry. Personalize-o de acordo com os requisitos específicos do seu projeto.
