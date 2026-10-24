import psycopg2 
def table():

    conn = psycopg2.connect(dbname = "postgres",user="postgres",password="S0h@ib12",host="localhost",port="5432")

    cursor = conn.cursor()
    cursor.execute(''' create table employees(Name text, ID int, Age int);''')

    print('Table creatd  Successfully!')

    conn.commit()
    conn.close()
def data():
    conn = psycopg2.connect(dbname = "postgres",user="postgres",password="S0h@ib12",host="localhost",port="5432")

    cursor = conn.cursor()

    name = input("Enter name  : ")
    id = input("Enter id : ")
    age = input("Enter age : ")

    query = '''insert into employees(Name,ID,Age) values(%s,%s,%s);'''
    cursor.execute(query,(name,id,age))
    # cursor.execute('''insert into employees(Name,ID,Age) values('Sohaib',01,19);''')

    print('Table creatd  Successfully!')

    conn.commit()
    conn.close()
data()
# print("Hello Sohaib!")

def execute():
    conn = psycopg2.connect(dbname = "postgres",user="postgres",password="S0h@ib12",host="localhost",port="5432")

    cursor = conn.cursor()
    cursor.execute('''SELECT * FROM EMPLOYEES;''')
    # show = cursor.fetchone()
    print(cursor.fetchone())
    # print(show[1]) # indexing
    
    # print('Table creatd  Successfully!')
    

    conn.commit()
    conn.close()   
execute() 