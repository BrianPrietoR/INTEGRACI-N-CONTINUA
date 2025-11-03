from flask import Flask
import mysql.connector
import time
import os

app = Flask(__name__)

DB_HOST = os.environ.get("DB_HOST", "db")
DB_USER = os.environ.get("DB_USER", "user")
DB_PASSWORD = os.environ.get("DB_PASSWORD", "password")
DB_NAME = os.environ.get("DB_NAME", "testdb")

def get_connection(retries=10, delay=3):
    for i in range(retries):
        try:
            conn = mysql.connector.connect(
                host=DB_HOST,
                user=DB_USER,
                password=DB_PASSWORD,
                database=DB_NAME
            )
            return conn
        except Exception as e:
            print(f"Intento {i+1}/{retries}: DB no lista ({e}). Esperando {delay}s...")
            time.sleep(delay)
    raise Exception("No se pudo conectar a la base de datos después de varios intentos.")

@app.route("/")
def home():
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS visitas (id INT AUTO_INCREMENT PRIMARY KEY, ts TIMESTAMP DEFAULT CURRENT_TIMESTAMP)")
        cursor.execute("INSERT INTO visitas VALUES (NULL, DEFAULT)")
        conn.commit()
        cursor.execute("SELECT COUNT(*) FROM visitas")
        count = cursor.fetchone()[0]
        cursor.close()
        conn.close()
        return f"Conexión a la base de datos EXITOSA. Visitas totales: {count}"
    except Exception as e:
        return f"No se pudo conectar a la base de datos: {e}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
