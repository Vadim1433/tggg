import sqlite3 as sq

db = sq.connect('tg.db')
cur = db.cursor()


async def bd_start():
    cur.execute('CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY AUTOINCREMENT, tg_id INTEGER, name TEXT)')
    db.commit()

async def cmd_start_db(user_id):
    user = cur.execute('SELECT * FROM users WHERE tg_id == {key}'.format(key=user_id)).fetchone()
    if not user:
        cur.execute('INSERT INTO users (tg_id) VALUES ({key})'.format(key=user_id))
        db.commit()