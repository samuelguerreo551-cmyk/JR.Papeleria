import sqlite3

DB_NAME = "papeleria.db"


def conectar():
    return sqlite3.connect(DB_NAME)


def crear_tablas():
    conn = conectar()
    cursor = conn.cursor()

    # ============================
    # TABLA USUARIOS
    # ============================
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS usuarios(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        usuario TEXT UNIQUE NOT NULL,
        contrasena TEXT NOT NULL,
        rol TEXT NOT NULL
    )
    """)

    # ============================
    # TABLA CATEGORIAS
    # ============================
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS categorias(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT UNIQUE NOT NULL
    )
    """)

    # ============================
    # TABLA PRODUCTOS
    # ============================
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS productos(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        categoria_id INTEGER,
        precio REAL NOT NULL,
        stock INTEGER NOT NULL,
        stock_minimo INTEGER NOT NULL,
        FOREIGN KEY(categoria_id) REFERENCES categorias(id)
    )
    """)

    # ============================
    # TABLA VENTAS
    # ============================
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS ventas(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        fecha DATETIME DEFAULT CURRENT_TIMESTAMP,
        total REAL NOT NULL
    )
    """)

    # ============================
    # DETALLE DE VENTAS
    # ============================
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS detalle_ventas(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        venta_id INTEGER,
        producto_id INTEGER,
        cantidad INTEGER,
        precio REAL,
        subtotal REAL,
        FOREIGN KEY(venta_id) REFERENCES ventas(id),
        FOREIGN KEY(producto_id) REFERENCES productos(id)
    )
    """)

    # ============================
    # SERVICIOS
    # ============================
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS servicios(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        tipo TEXT,
        descripcion TEXT,
        precio REAL,
        fecha DATETIME DEFAULT CURRENT_TIMESTAMP
    )
    """)

    # ============================
    # ENTRADAS DE INVENTARIO
    # ============================
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS entradas_inventario(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        producto_id INTEGER,
        cantidad INTEGER,
        fecha DATETIME DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY(producto_id) REFERENCES productos(id)
    )
    """)

    # ============================
    # USUARIO ADMINISTRADOR
    # ============================
    cursor.execute("""
    SELECT * FROM usuarios
    WHERE usuario='admin'
    """)

    if cursor.fetchone() is None:
        cursor.execute("""
        INSERT INTO usuarios
        (nombre, usuario, contrasena, rol)
        VALUES
        ('Administrador', 'admin', 'admin123', 'Administrador')
        """)

    conn.commit()
    conn.close()

    print("Base de datos creada correctamente.")


if __name__ == "__main__":
    crear_tablas()