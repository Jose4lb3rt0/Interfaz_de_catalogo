import mysql.connector

class Registro_Datos:

    def __init__(self):
        try:
            # Reemplaza 'user', 'password', 'host', y 'database' con tus propios valores
            self.conexion = mysql.connector.connect(
                user='root',
                password='admin',
                host='localhost',
                database='interfaz_de_catalogo'
            )

            if self.conexion.is_connected():
                print("¡Conexión exitosa!")

        except mysql.connector.Error as err:
            print(f"Tienes un error: {err}")


    def __del__(self):
        # Cierra la conexión al destruir la instancia
        if hasattr(self, 'conexion') and self.conexion.is_connected():
            self.conexion.close()


    def inserta_producto(self, codigo, nombre, modelo, precio, cantidad):
        cur = self.conexion.cursor()
        sql = '''INSERT INTO productos (CODIGO, NOMBRE, MODELO, PRECIO, CANTIDAD)
                VALUES('{}', '{}', '{}', '{}', '{}')'''.format(codigo, nombre, modelo, precio, cantidad)
        cur.execute(sql)
        self.conexion.commit()
        cur.close()


    def buscar_productos(self):
        cursor = self.conexion.cursor()
        sql = "SELECT * FROM productos"
        cursor.execute(sql)
        registro = cursor.fetchall()
        return registro

    def busca_producto(self, nombre_producto):
        cur = self.conexion.cursor()
        sql = "SELECT * FROM productos WHERE NOMBRE = {}".format(nombre_producto)
        cur.execute(sql)
        nombreX = cur.fetchall()
        cur.close()
        return nombreX

    def carga_producto(self, codigo_producto):
        cur = self.conexion.cursor()
        sql = "SELECT nombre, modelo, precio, cantidad FROM productos WHERE CODIGO = {}".format(codigo_producto)
        cur.execute(sql)
        codigoX = cur.fetchall()
        cur.close()
        return codigoX


    def elimina_productos(self, nombre):
        cur = self.conexion.cursor()
        sql = '''DELETE FROM productos WHERE NOMBRE = {}'''.format(nombre)
        cur.execute(sql)
        a = cur.rowcount
        self.conexion.commit()
        return a


    def actualiza_productos(self, codigo, nombre, modelo, precio, cantidad):
        cur = self.conexion.cursor()
        sql = '''UPDATE productos SET NOMBRE = '{}', MODELO = '{}', PRECIO = '{}', CANTIDAD = '{}' WHERE CODIGO = '{}' '''.format(nombre, modelo, precio, cantidad, codigo)
        cur.execute(sql)
        a = cur.rowcount
        self.conexion.commit()
        cur.close()
        return a

# Ejemplo de uso de la clase RegistroDatos
#conexion_registro = RegistroDatos()
#conexion_registro.inserta_producto('123', 'Producto1', 'Modelo1', '10.99', '50')
#resultados = conexion_registro.buscar_productos()
#print(resultados)
