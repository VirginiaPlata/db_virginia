import mysql.connector

# Conexión
conn = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="clase123",
    database="escuela_db"
)

cursor = conn.cursor()


# -----------------------------------
# EJERCICIO 1 - INSERTAR ESTUDIANTES
# -----------------------------------

print("\n--- EJERCICIO 1 ---")

cursor.execute("""
INSERT INTO estudiantes (nombre, edad, carrera)
VALUES ('Virginia Valenzuela', 24, 'Desarrollo de Software'),
       ('Luis Martínez', 21, 'Arquitectura'),
       ('Fernanda Gómez', 23, 'Contabilidad')
""")

conn.commit()

cursor.execute("SELECT * FROM estudiantes")

for fila in cursor.fetchall():
    print(fila)

# -----------------------------------
# EJERCICIO 2 - SELECT CON WHERE
# -----------------------------------

print("\n--- EJERCICIO 2 ---")

cursor.execute("""
SELECT * FROM estudiantes
WHERE carrera = 'Medicina'
""")

for fila in cursor.fetchall():
    print(fila)


# -----------------------------------
# EJERCICIO 3 - TABLA PROFESORES
# -----------------------------------

print("\n--- EJERCICIO 3 ---")

cursor.execute("""
CREATE TABLE IF NOT EXISTS profesores (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    materia VARCHAR(100),
    email VARCHAR(100)
)
""")


cursor.execute("""
INSERT INTO profesores (nombre, materia, email)
VALUES ('Laura Pérez', 'Base de Datos', 'laura@correo.com'),
       ('Miguel Sánchez', 'Programación Web', 'miguel@correo.com')        
""")

conn.commit()

cursor.execute("SELECT * FROM profesores")

for fila in cursor.fetchall():
    print(fila)


# -----------------------------------
# EJERCICIO 4 - UPDATE Y DELETE
# -----------------------------------

print("\n--- EJERCICIO 4 ---")

cursor.execute("""
UPDATE estudiantes
SET edad = 21
WHERE nombre = 'Ana López'
""")


cursor.execute("""
DELETE FROM estudiantes
WHERE nombre = 'Carlos Ruiz'
""")

conn.commit()

cursor.execute("""
SELECT * FROM estudiantes
""")

for fila in cursor.fetchall():
    print(fila)


cursor.close()
conn.close()