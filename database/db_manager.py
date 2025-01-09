import sqlite3

def create_table(conn):
    cursor = conn.cursor()
    try:
        cursor.execute('''
            CREATE TABLE users (
                name TEXT,
                middle_name TEXT,
                last_name TEXT
            )
        ''')
    except sqlite3.OperationalError:
        pass
def insert_user(conn, name, middle_name, last_name ):
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (name, middle_name,last_name) VALUES (?, ?, ?)", (name, middle_name, last_name))
    conn.commit()
    print("Database created")

if __name__ == "__main__":
    conn = sqlite3.connect('data.db')
    create_table(conn)
    insert_user(conn, 'Riccardo', 'Calafiori','Orozco')
    insert_user(conn, 'Darwin', 'Nuñez','Castro')
    insert_user(conn, 'Lamine', 'Yamal','Ebana')

    conn.close()



