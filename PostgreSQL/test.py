import psycopg2 
def table():

    conn = psycopg2.connect(dbname = "postgres",user="postgres",password="S0h@ib12",host="localhost",port="5432")

    cursor = conn.cursor()
    cursor.execute(''' create table employees(Nmae text, ID int, Age int);''')

    print('Table creatd  Successfully!')

    conn.commit()
    conn.close()
def data():
    conn = psycopg2.connect(dbname ='postgres',user ='postgres', password = 'S0h@ib12')


# print("Hello Sohaib!")
