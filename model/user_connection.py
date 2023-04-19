import psycopg2

class UserConnection():
    
    conn = None
    
    def __init__(self):
        try:
            self.conn = psycopg2.connect("dbname=database user=admin password=1234 host=db port=5432")
        except psycopg2.OperationalError as err:
            print(err)
            self.conn.close()


    def write(self, data):
        with self.conn.cursor() as cur:
            cur.execute("""
                INSERT INTO "user"(name, phone)
                VALUES(%(name)s, %(phone)s)
            """, data)

        self.conn.commit()


    def __def__(self):
        self.conn.close()