import psycopg2 

DB_HOST = "localhost"
DB_PORT = "5432"
DB_NAME = "demo_cleaningdb"
DB_USER = "postgres"
DB_PASSWORD = "qzmpg*"
# DB_URL = "postgresql://postgres:admin@localhost:5432/demo_cleaningdb"

try:
    # connect to postgresql database 
    connection = psycopg2.connect(
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
        host=DB_HOST,
        port=DB_PORT
    )  
    cursor = connection.cursor()
    print("Postgresql Connection Successfull")

    # execute a test query 
    cursor.execute("SELECT table_name FROM information_schema.tables WHERE table_name = 'public';")
    tables = cursor.fetchall()
    print("Tables in the database:")
    for table in tables:
        print(table[0])

    # close connection
    cursor.close()
    connection.close()
    print("Connection Closed.")

except Exception as e:
    print(f"Error connecting to Postgresql: {e}")

