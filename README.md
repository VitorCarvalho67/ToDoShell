<div align="center">
  <img src="https://github.com/VitorCarvalho67/ToDoShell/assets/102667323/22ead2a9-f87b-4728-83b5-b3e3ccc55eeb" />
</div>

This Python project is a robust and feature-rich ToDoList application, built entirely using object-oriented programming and employing asynchronous techniques. It harnesses the capabilities of MySQL, Python, Prisma, and Poetry to provide users with a seamless task management system. Users can easily register, log in, and once logged in, they have the flexibility to create new tasks, complete with titles and descriptions. From the main menu, users can efficiently list all their tasks, add new ones, remove existing tasks, and log out. This project showcases the power of object-oriented design and async programming, combining Python for the backend, MySQL for data storage, Prisma for database management, and Poetry for dependency management, ensuring a responsive and user-friendly experience.

## How to use:

1. **Clone the Repository:**

```
git clone https://github.com/VitorCarvalho67/ToDoShell.git
```

2. **Navigate to the Project Folder:**

```
cd ToDoShell
```

3. **Install Dependencies with Poetry or Run venv Directly**

Use the following command to install the dependencies listed in the `pyproject.toml` file:

```
poetry install
```

or

```
python -m venv venv
# Windows
.\venv\Scripts\activate.bat
# Linux and *nix
. ./venv/bin/activate
# Install dependencies
pip install -r requirements.txt
```

3.1. **(Optional) Start the database with docker-compose**
Docker must be installed on your machine

```
docker-compose up -d
```

4. **Migrate the Prisma database**
You need to migrate the Prisma database for tables to be created

```
prisma db push
```

5. **Run the Project:**

Run your Python project with Poetry. Replace `main.py` with the name of your project's main file:

```
poetry shell
python main.py
```

or

```
# Inside the venv
(venv) $ python main.py
```

This will start your project.
>[!IMPORTANT]
> remember to uncomment .env.example and remove .example from the file name.

## Screenshots:

![Screenshot_297](https://github.com/VitorCarvalho67/ToDoShell/assets/102667323/523ca199-ed72-48a5-8c6c-d00a052ae6ef)


Make sure Prisma settings and environment variables are properly configured in your project as specified in the Prisma documentation. This simple guide should help you set up and run your project with Prisma as a dependency using Poetry. Customize it as per your project's specific requirements.
