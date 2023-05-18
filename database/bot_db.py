import random
import sqlite3


def sql_create():
    global db, cursor
    db = sqlite3.connect('bot.db')
    cursor = db.cursor()

    if db:
        print("База данных подключена!")

    db.execute(
        "CREATE TABLE IF NOT EXISTS mentors "
        "(id INTEGER PRIMARY KEY, name TEXT, "
        "name VARCHAR (200),"
        "direction VARCHAR (200), "
        "age INTEGER, "
        "group1 TEXT)")
    db.commit()


async def sql_command_insert(state):
    async with state.proxy() as data:
        cursor.execute(
            "INSERT INTO mentors "
            "(name, direction, age, group1) "
            "VALUES (?, ?, ?, ?)",
            tuple(data.values())
        )
        db.commit()


async def sql_command_random():
    users = cursor.execute("SELECT * FROM mentors").fetchall()
    random_user = random.choice(users)
    return random_user


async def sql_command_delete(id: str):
    cursor.execute("DELETE FROM mentors WHERE id = ?", (id,))
    db.commit()


async def sql_command_all():
    return cursor.execute("SELECT * FROM mentors").fetchall()
