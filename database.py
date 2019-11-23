import psycopg2, os

CRED_USER = os.getenv('POSTGRES_USER')
CRED_PWD = os.getenv('POSTGRES_PWD')
CRED_HOST = os.getenv('POSTGRES_HOST')
CRED_PORT = os.getenv('POSTGRES_PORT')
CRED_DB = os.getenv('POSTGRES_DB')

class database:

    def __init__(self):
        try:
            self.connection = psycopg2.connect(user=CRED_USER,password=CRED_PWD,host=CRED_HOST,port=CRED_PORT,database=CRED_DB)
            self.cursor = self.connection.cursor()
            #print ( self.connection.get_dsn_parameters(),"\n")
            #print('[PostgreSQL] Version:',cursor.execute("SELECT version();"))
            self.record = cursor.fetchone()
            print("[PostgreSQL] Connected to - ", self.record,"\n")

        except (Exception, psycopg2.Error) as error :
            print ("[PostgreSQL] Error while connecting to the database", error)

    def overwrite(self, *args):
        print('Hello World')

    def read(self):
        print('Hello World')

    def __del__(self):
        #closing database connection.
        if(self.connection):
            self.cursor.close()
            self.connection.close()
            print("[PostgreSQL] connection is closed")
