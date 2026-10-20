import sqlite3 
def db():
    con = sqlite3.connect("interactive_quiz")
    cur = con.cursor()
    cur.execute('''
     CREATE TABLE IF NOT EXISTS USERS(
        id INTEGER PRIMARY KEY,
        email TEXT UNIQUE,
        passwd TEXT NOT NULL,
        role TEXT NOT NULL
     )
    ''')

    cur.execute('''
        CREATE TABLE IF NOT EXISTS quiz_attempts(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_email TEXT NOT NULL,
            score INTEGER NOT NULL,
            topic_weakness TEXT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    

    con.commit()
    con.close()
    print("Database and both tables created successfully!")

if __name__ == '__main__':
    db()
