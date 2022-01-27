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
