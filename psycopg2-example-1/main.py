#Required pip pkg(s)
#pip install psycopg2-binary
#pip install configparser

import psycopg2, psycopg2.extras
from config import config


def connect():
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
    
    








# using 'with' Class
params = config()
conn = None
cur = None
try:

    with psycopg2.connect(**params) as conn:
    
        #1: cursor_factory=psycopg2.extras.DictCursor => returns in form of dict..
        with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:
    
            cur.execute('DROP TABLE IF EXISTS employee')

            create_script = ''' CREATE TABLE IF NOT EXISTS employee (
                                            id      int PRIMARY KEY,
                                            name    varchar(40) NOT NULL,
                                            salary  int,
                                            dept_id varchar(30)) '''
            cur.execute(create_script)

            insert_script = 'INSERT INTO employee (id, name, salary, dept_id) VALUES (%s, %s, %s, %s)'
            insert_values = [(1, 'James', 12000, 'D1'), (2, 'Scott', 13000, 'D1'), (3, 'Jim', 12500, 'D2')]

            for record in insert_values:
                cur.execute(insert_script, record)

            # Update salary example
            update_script = 'UPDATE employee SET salary = salary + (salary * 0.5)'
            cur.execute(update_script)


            cur.execute('SELECT * FROM EMPLOYEE')
            for record in cur.fetchall():
                #Ref #1 above cur=conn......
                print(record['name'], record['salary'])


            delete_script = 'DELETE FROM employee WHERE name = %s'
            delete_record = ('James',)
            cur.execute(delete_script, delete_record)
            print('{name} is deleted'.format(name=delete_record))
            
            
            cur.execute('SELECT * FROM EMPLOYEE')
            for record in cur.fetchall():
                #Ref #1 above cur=conn......
                print(record['name'], record['salary'])
            print("Record updated")
            # not needed for 'with' CLass
            #conn.commit()
            
            # not needed for try,except,finally
            #cur.close()
            #conn.close()

except Exception as error:
    print(error)
    
finally:
    # not needed for 'with' CLass
    #if cur is not None:
        #cur.close()
    if conn is not None:
        conn.close()
        print("connection closed")

