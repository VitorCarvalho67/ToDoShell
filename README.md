# ToDoShell

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

Certifique-se de que as configurações do Prisma e as variáveis de ambiente estejam devidamente configuradas em seu projeto, como especificado na documentação do Prisma. Este guia simples deve ajudá-lo a configurar e executar seu projeto com o Prisma como dependência usando Poetry. Personalize-o de acordo com os requisitos específicos do seu projeto.
