import sqlite3


class Database:
    def __init__(self):
        self.name = "todo.db"
        with sqlite3.connect(self.name) as conn:
            c = conn.cursor()

            c.execute("""CREATE TABLE IF NOT EXISTS todos 
                (
                todo TEXT,
                is_done BOOL
                )

            """)

            conn.commit()


    def add(self, todo, status):
        with sqlite3.connect(self.name) as conn:
            c = conn.cursor()
            c.execute("""INSERT INTO todos VALUES (?, ?)""", (todo, status) )
            conn.commit()
            print("added")
        

    def delete(self, text):
        with sqlite3.connect(self.name) as conn:
            c = conn.cursor()
            c.execute("""DELETE FROM todos WHERE todo = ? """, [text] )
            conn.commit()
            print("deleted")
            
    def change_status(self, text, status):
        with sqlite3.connect(self.name) as conn:
            c = conn.cursor()
            c.execute("""UPDATE todos SET is_done = ? WHERE todo = ? """, (status, text) )
            conn.commit()
            print("updated")

    def delete_all(self):
        with sqlite3.connect(self.name) as conn:
            c = conn.cursor()
            c.execute("""DELETE FROM todos""")
            conn.commit()
            print("all deleted")

    def get_all(self):
        with sqlite3.connect(self.name) as conn:
            c = conn.cursor()
            c.execute(""" SELECT * from todos""")
            todos = c.fetchall()
            return todos