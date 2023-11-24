import pyodbc

def db_connect():
    server = '10.10.10.233'
    database = 'OptimusNT_sincro'
    username = 'sa'
    password = '25ghost06!'

    global table
    table = 'tab_import_composizione_fasci'

    global connection
    connection = pyodbc.connect('DRIVER={SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+password)

def db_select_all():
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM " + table)
    rows = cursor.fetchall()

    for row in rows:
        print(row)
    cursor.close()

def test_insert(df):
    # Define your SQL INSERT statement
    cursor = connection.cursor()

    for index, row in df.iterrows():
        cursor.execute("INSERT INTO " + table + " (d_interno, d_esterno, lunghezza, ascissa, ordinata, composizione, num_pezzi_strato, forma_fascio, guid, altezza_max) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", row['d_int'], row['d_est'], row['lunghezza'], row['ascissa'], row['ordinata'], row['composizione_fascio'], row['num_pezzi_strato'], row['forma_fascio'], row['uuid'], row['altezza_max'])
        print(row)

    connection.commit()
    cursor.close()

    
    

def close_connection():

    db_select_all()
    connection.close()
    
