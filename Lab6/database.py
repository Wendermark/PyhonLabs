import sqlite3

connection = sqlite3.connect('telegramBot.db', check_same_thread=False)

cursor = connection.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS users(
    id INTEGER NOT NULL,
    name TEXT NOT NULL,
    score INTEGER NOT NULL DEFAULT 0
)""")

connection.commit()

def save_score(id, score):
    bestScore = cursor.execute("SELECT score FROM users WHERE id = ?", (id,)).fetchone()[0]

    if score > bestScore:
        cursor.execute("UPDATE users SET score = ? WHERE id = ?", (score, id,))

        connection.commit()

def register_user(id:int, name:str):

    if(cursor.execute("SELECT * FROM users WHERE id = ?", (id,)).fetchone() != None):
        return
    
    cursor.execute("INSERT INTO users(id, name) VALUES(?, ?)", (id, name,))

    connection.commit()

def get_top_score():
    return cursor.execute("SELECT * FROM users ORDER BY score LIMIT 10").fetchall()