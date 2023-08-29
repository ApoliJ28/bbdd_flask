import pymysql

def get_conn():
    return pymysql.connect(
        host="localhost",
        user = "root",
        password= "1234",
        db= "basedatos_flask"
    )

def insertar_articulo(nombre, precio):
    conn = get_conn()
    
    with conn.cursor() as cursor:
        cursor.execute(f"INSERT INTO articulos (nombre, precio)  VALUES ('{nombre}', '{precio}');")
        conn.commit()
        cursor.close()
    conn.close()

def listar_articulos():
    conn = get_conn()
    articulos = []
    with conn.cursor() as cursor:
        cursor.execute("SELECT  id, nombre, precio FROM articulos;")
        articulos = cursor.fetchall()
        cursor.close()
    conn.close()
    return articulos

def eliminar_articulo(id):
    conn = get_conn()
    with conn.cursor() as cursor:
        cursor.execute(f"DELETE FROM articulos WHERE id = '{id}'")
        conn.commit()
        cursor.close()
    conn.close()

def get_articulo(id):
    conn = get_conn()
    articulo = None
    with conn.cursor() as cursor:
        cursor.execute(f"SELECT * FROM articulos WHERE id = '{id}'")
        articulo = cursor.fetchone()
        cursor.close()
    conn.close()
    return articulo

def actualizar_articulo(id, nombre, precio):
    conn = get_conn()
    with conn.cursor() as cursor:
        cursor.execute(f"UPDATE articulos set nombre = '{nombre}', precio = '{precio}' WHERE id = '{id}' ")
        conn.commit()
    conn.close()


