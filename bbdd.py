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
        cursor.execute(f"INSERT INTO articulos (nombre, precio)  VALUES ({nombre}, {precio});")
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

def eliminar_articulos(id):
    conn = get_conn()
    with conn.cursor() as cursor:
        cursor.execute(f"DELETE FROM articulos WHERE id = {id}")
        conn.commit()
        cursor.close()
    conn.close()

if __name__ == '__main__':
    articulos = listar_articulos()
    print(articulos)
