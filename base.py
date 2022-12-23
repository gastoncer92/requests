import sqlite3
from sqlite3 import Error


def conexion():
    try:
        conn = sqlite3.connect('base1.db')
        cursor = conn.cursor()
        cursor.execute('PRAGMA foreign_keys = ON')
        conn.commit()
        return conn
    except Error:
        print(Error)


def dbCorreos():
    ''' Creacion de base de datos para los correos '''
    conn = conexion()
    cursor = conn.cursor()
    cursor.executescript("""
    CREATE TABLE IF NOT EXISTS [TablaCorreo] (
        [idCorreo] INTEGER  NOT NULL PRIMARY KEY AUTOINCREMENT,
        [correo] VARCHAR(250)  NULL
)
    """)
    conn.commit()
    conn.close()


def CantidadCorreos():
    conn = conexion()
    cursor = conn.cursor()
    cantidadCorreos = cursor.execute("select count(idCorreo) from TablaCorreo;").fetchall()[0][0]
    conn.close()
    return cantidadCorreos

def yaExisteCorreo(correo):
    conn = conexion()
    cursor = conn.cursor()
    dato = cursor.execute('SELECT EXISTS (SELECT correo from TablaCorreo WHERE correo=(?));',
                          (correo,)).fetchall()[0][0]
    print(',,,,,,,,,,,,,,,')
    print(dato)
    ## retorna 1 si existe y 0 sino
    print(',,,,,,,,,,,,,,,')
    conn.close()
    if dato == 1:
        print('existe')
        return True
    else:
        print('no existe')
        return False


def CargarProducto(dato):
    conn = conexion()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO TablaCorreo (idCorreo,correo) VALUES (?,?);',dato, )
    try:
        conn.commit()
    except Error:
        conn.rollback()
    conn.close()


def TodosLosCorreos(conn):
    # conn = conexion()
    cursor = conn.cursor()
    resultado = cursor.execute('select correo from TablaCorreo').fetchall()

    return resultado
