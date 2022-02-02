from mysql import connector

from db.conexion import create_connection


def insert(data):
    conn = create_connection()
    sql= """ INSERT INTO recipes (
        title,
        category,
        guide_url,
        budget,
        img_path,
        ingredients,
        directions 
    )
    VALUES(%s, %s, %s, %s, %s, %s, %s)
    """
    
    try:
        cur = conn.cursor()
        cur.execute(sql, data)
        conn.commit()
        return True
    except connector.Error as err:
        print(f"Error at insert_recurse function: {err.msg}")
        return False
    finally:
        cur.close()
        conn.close()

def select_all():
    conn = create_connection()
    sql= """ SELECT id, img_path, title, category FROM recipes"""
    
    try:
        cur = conn.cursor()
        cur.execute(sql)
        recipes = cur.fetchall()
        return recipes
    except connector.Error as err:
        print(f"Error at select_all function: {err.msg}")
        return False
    finally:
        cur.close()
        conn.close()