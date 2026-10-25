import sqlite3

def db():
    con = sqlite3.connect("interactive_quiz.db")
    cur = con.cursor()


    cur.execute('''
        CREATE TABLE IF NOT EXISTS users(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            passwd TEXT NOT NULL,
            role TEXT NOT NULL,
            streak INTEGER DEFAULT 0
        )
    ''')

  
    cur.execute('''
        CREATE TABLE IF NOT EXISTS quizzes(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL
        )
    ''')

  
    cur.execute('''
        CREATE TABLE IF NOT EXISTS questions(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            quiz_id INTEGER,
            topic TEXT NOT NULL,
            question_text TEXT NOT NULL,
            option_a TEXT NOT NULL,
            option_b TEXT NOT NULL,
            option_c TEXT NOT NULL,
            option_d TEXT NOT NULL,
            correct_option TEXT NOT NULL,
            difficulty TEXT DEFAULT 'Easy',
            FOREIGN KEY(quiz_id) REFERENCES quizzes(id)
        )
    ''')

   
    cur.execute('''
        CREATE TABLE IF NOT EXISTS quiz_attempts(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_email TEXT NOT NULL,
            quiz_id INTEGER,
            score INTEGER NOT NULL,
            total_questions INTEGER NOT NULL,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY(user_email) REFERENCES users(email),
            FOREIGN KEY(quiz_id) REFERENCES quizzes(id)
        )
    ''')

  
    cur.execute('''
        CREATE TABLE IF NOT EXISTS attempt_details(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            attempt_id INTEGER,
            question_id INTEGER,
            selected_answer TEXT,
            confidence_level TEXT,
            is_correct BOOLEAN,
            FOREIGN KEY(attempt_id) REFERENCES quiz_attempts(id),
            FOREIGN KEY(question_id) REFERENCES questions(id)
        )
    ''')

    con.commit()
    con.close()
    print("Full database structure created successfully!")

if __name__ == '__main__':
    db()
