def connect():
    connection = None
    try:
        params = config()
        print("connecting to db...")
        connection = psycopg2.connect(**params)

        # create a cursor
        crsr = connection.cursor()
        print('create db:')
        crsr.execute('CREATE DATABASE master')
        db_create = crsr.fetchone()
        print(db_create)
        crsr.close()
        
    except(Exception, psycopg2.DatabaseError) as error:
        print(error)
        
    finally:
        if connection is not None:
            
            connection.close()
            print('db session quit')
if __name__ == "__main__":
    connect()