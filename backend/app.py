from flask import Flask
import psycopg2
import os
from dotenv import load_dotenv

# Cargar las variables del archivo .env
load_dotenv()

app = Flask(__name__)

def get_conn():
    return psycopg2.connect(
        host=os.getenv("DB_HOST"),
        database=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD")
    )

@app.route("/")
def home():
    try:
        conn = get_conn()
        conn.close()
        return {"msg": "Conexión a PostgreSQL funcionando correctamente!"}
    except Exception as e:
        return {"error": str(e)}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
