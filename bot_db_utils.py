import psycopg2
from datetime import datetime

def connect_postgres():
    conn = psycopg2.connect(host='localhost', 
    port=5434, 
    user='postgres', 
    password='postgres',
    database='test_db', 
    )
    return conn

def save_search_data(author_id, query_keyword, links):
	connection = connect_postgres()
	cursor = connection.cursor()
	cursor.execute("Insert into bot_data Values('{}', '{}', '{}', '{}')".format(
        author_id, query_keyword, datetime.now().strftime("%Y-%m-%d %H:%M:%S"), links))
	connection.commit()
	connection.close()

def fetch_data(author_id, query_keyword):
	connection = connect_postgres()
	cursor = connection.cursor()
	cursor.execute("select * from bot_data where user_id = '{}' and query like '%".format(author_id) + query_keyword +"%'")
	results = cursor.fetchall()
	connection.close()
	return results
