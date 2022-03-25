def connect():
    connection = None
    try:
        params = config()
        print("connecting to db...")
        connection = psycopg2.connect(**params)

        # create a cursor
        crsr = connection.cursor()
        print('db create:')
        crsr.execute("CREATE TABLE cars (id serial PRIMARY KEY, year integer, make varchar, model varchar);")
        connection.commit()
                                                    
        crsr.execute("SELECT * FROM cars;")
        dt_table = None
        db_table = crsr.fetchone()
        if dt_table == None:
            print('successful')
        crsr.close()
        
    except(Exception, psycopg2.DatabaseError) as error:
        print(error)
        
    finally:
        if connection is not None:
            
            connection.close()
            print('db session quit')
if __name__ == "__main__":
    connect()
