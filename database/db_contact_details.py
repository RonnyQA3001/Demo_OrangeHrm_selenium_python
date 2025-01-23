import sqlite3



def create_contact_details_table(conn):
    cursor = conn.cursor()
    try:
        cursor.execute('''
            CREATE TABLE contact_table (
                street1 TEXT,
                city TEXT,
                state TEXT,
                zip_code TEXT,
                mobile_number TEXT,
                work_number TEXT,
                work_email TEXT,
                other_email TEXT
                
            )
        ''')
    except sqlite3.OperationalError:
        pass

def insert_contact_details(conn,street1,city,state,zip_code,mobile_number,work_number,work_email,other_email):
    cursor = conn.cursor()
    cursor.execute("INSERT INTO contact_table(street1,city,state,zip_code,mobile_number,work_number,work_email,other_email) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",(street1,city,state,zip_code,mobile_number,work_number,work_email,other_email))
    conn.commit()
    print("Database created")

if __name__ == "__main__":
    conn = sqlite3.connect('contact_details.db')
    create_contact_details_table(conn)
    insert_contact_details(conn,'Rruga Dritan Hoxha','Tirana','Tirana','2930','355-040-9384','504-286-5815','riccardoc01@company.com','ricc29c@gmail.com')
    insert_contact_details(conn,'3381 Holt Street','Chetopa','Kansas','67366','561-387-4561','627-309-0937','darwinn02@company.com','darww09n2@gmail.com')
    insert_contact_details(conn,'Prolongacion San Sebastian 53','Perez','Huelva','21100','712-211-1664','245-356-0242','laminy03@company.com','lamn53y@gmail.com')

    conn.close()