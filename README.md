# ToDoShell

## How to Use
This guide outlines how to set up and use "My Project." Follow these steps to get started.

you need poetry installed

```bash
pip install poetry
```

For start you need add .env file with your credentials

```bash
cp .env.example .env
```

And after you add on your terminal

```bash
poetry shell
```

Updade your poetry

```bash
poetry update package
```

And after you add on your terminal

```bash
poetry install
```
Add prisma to your project

```bash
poetry add prisma
```

Make migrations

```bash
prisma db push
```

Run server

```bash
python main.py
```
