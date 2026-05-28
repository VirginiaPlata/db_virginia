
import sqlite3

conn = sqlite3.connect("test.db")
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS clientes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        telefono TEXT
    )
""")

cursor.execute("""
    INSERT INTO clientes (nombre, telefono)
    VALUES ('Virginia Valenzuela', '664-366-2112')
""")


conn.commit()
conn.close()