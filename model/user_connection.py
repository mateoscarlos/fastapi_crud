import psycopg2

class UserConnection():
    
    conn = None
    
    def __init__(self):
        try:
            self.conn = psycopg2.connect("dbname=database user=admin password=1234 host=db port=5432")
        except psycopg2.OperationalError as err:
            print(err)
            self.conn.rollback()


    def write(self, data):
        with self.conn.cursor() as cur:
            cur.execute("""
                INSERT INTO "user"(name, phone)
                VALUES(%(name)s, %(phone)s)
            """, data)

        self.conn.commit()


    def read_all(self):
        with self.conn.cursor() as cur:
            cur.execute("""
                SELECT * FROM "user"
            """)

            return cur.fetchall()
        

    def read(self, id):
        with self.conn.cursor() as cur:
            cur.execute("""
                SELECT * FROM "user" WHERE id = %s
            """, (id,))
            
            return cur.fetchone()


    def update(self, data):
        with self.conn.cursor() as cur:
            cur.execute("""
                UPDATE "user" 
                SET name = %(name)s, phone = %(phone)s
                WHERE id = %(id)s
            """, data)

        self.conn.commit()


    def delete(self, id):
        with self.conn.cursor() as cur:
            cur.execute("""
                DELETE FROM "user" WHERE id = %s
            """, (id,))

        self.conn.commit()


    def __def__(self):
        self.conn.close()