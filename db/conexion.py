from mysql import connector


config = {
    'user': 'root',
    #'password': 'Samimajo10',
    'host': 'localhost',
    'database': 'recipes_db'
}


def create_connection():
    conn = None
    try:
        conn = connector.connect(**config)
    except connector.Error as err:
        print(f"Error at create_connection function: {err.msg}")
    
    return conn