# APP.PY
# Aplicación con el código principal 

# Importa Flask
from flask import Flask

# Importa el driver para conectar la app a PostgreSQL
import psycopg2

# Importa el modulo de phyton necesario para que se pueda acceder a las dependencias del archivo requirements
import os

# Importa el módulo para cargar dichas variables 
from dotenv import load_dotenv

# Las carga
load_dotenv()

# Crea la app de Flask
app = Flask(__name__)

# Se encarga de crear y administrar la conexión con la db
def get_conn():
    return psycopg2.connect(
        host=os.getenv("DB_HOST"),                  # Dirección del host
        database=os.getenv("DB_NAME"),              # Nombre de la db
        user=os.getenv("DB_USER"),                  # Usario
        password=os.getenv("DB_PASSWORD")           # Contraseña 
    )

# Ruta de la api
@app.route("/")

# Maneja las conexiones con la db y también las excepciones en caso de que fallen
def home():
    try:
        conn = get_conn()
        conn.close()
        return {"msg": "Probando, 1, 2... Conexión a PostgreSQL funcionando correctamente!"}
    except Exception as e:
        return {"error": str(e)}


# Inicia la app utilizando los puertos configurados
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
