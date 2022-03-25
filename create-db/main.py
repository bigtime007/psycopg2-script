import psycopg2
from config import config



def connect():
    ''' 
    used to connect to DB and post ver#

    Example:
    connecting to db...
    db ver:
    ('PostgreSQL 12.10, compiled by Visual C++ build 1914, 64-bit',)
    db session quit
    '''
    connection = None
    try:
        params = config()
        print("connecting to db...")
        connection = psycopg2.connect(**params)

        # create a cursor
        crsr = connection.cursor()
        print('db ver:')
        crsr.execute('SELECT version()')
        db_version = crsr.fetchone()
        print(db_version)
        crsr.close()
        
    except(Exception, psycopg2.DatabaseError) as error:
        print(error)
        
    finally:
        if connection is not None:
            
            connection.close()
            print('db session quit')
if __name__ == "__main__":
    connect()