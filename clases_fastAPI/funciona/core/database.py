from typing import Generator #generator es una respuesta de una session
import logging

from sqlalchemy import create_engine, text, MetaData
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy.exc import SQLAlchemyError, OperationalError, DisconnectionError
from sqlalchemy.pool import QueuePool

from config import settings  #llamo setings todo lo que viene de ahi

# Configurar el módulo de logging de Python y se usa para crear un registrador de eventos (logger)
logger = logging.getLogger(__name__)#parametro privado (encapsulamiento)

# Crear el motor de base de datos con configuraciones óptimas
engine = create_engine( #resultado de esta funcion
    settings.DATABASE_URL,
    echo=True,           # Activar o desactivar el modo debug para imprimir en consola todas las sentencias SQL esrto es para que muestre los errores en consola
    pool_pre_ping=True,  # Verifica que las conexiones estén activas antes de usarlas
    pool_recycle=3600,   # Recicla conexiones después de una hora para evitar el error "connection has been closed"
    pool_size=10,        # Número máximo de conexiones permanentes en el pool
    max_overflow=20,     # Conexiones adicionales permitidas temporalmente cuando el pool está lleno
    pool_timeout=30,     # Tiempo máximo de espera para obtener una conexión del pool
    poolclass=QueuePool  # Clase de pool para manejo eficiente de conexiones
)

# Crear la fábrica de sesiones
# - autocommit=False: Los cambios solo se guardan cuando se hace commit explícitamente|si no se escribe commit no inserta informacion en la base de datos
# - autoflush=False: Las operaciones pendientes solo se envían a la BD cuando se hace flush explícitamente
# - bind=engine: Vincula la sesión al motor creado anteriormente
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)#utilliza respuesta que llega de engine

# Declarar la base para los modelos ORM
Base = declarative_base()

# Instancia de MetaData para trabajar con tablas
metadata = MetaData()

def get_db() -> Generator:
    """
    Dependencia para obtener una sesión de base de datos en FastAPI.
    
    Crea una nueva sesión por cada solicitud y la cierra automáticamente
    al finalizar, incluso si ocurre alguna excepción.
    
    Yields:
        Session: Una sesión de SQLAlchemy para interactuar con la base de datos.
    
    Example:
        ```python
        @app.get("/items/")
        def read_items(db: Session = Depends(get_db)):
            return db.query(Item).all()
        ```
    """
    db = SessionLocal() #guardar lo de sesion en db ,y lo de abajpo son promesas y try es como decirle que espere respuestas
    try:
        yield db  # El 'yield' permite que la función de endpoint use la sesión.
    except SQLAlchemyError as e:
        db.rollback() # revierte todos los cambios en la base de datos
        logger.error(f"Error de base de datos: {str(e)}")
        raise # Propaga la excepción para que FastAPI pueda manejarla
    finally:
        db.close() # Cierra la sesión de base de datos y libera los recursos asociados.
        # Esto es esencial para evitar fugas de memoria y conexiones abiertas.


def check_database_connection() -> bool:
    """
    Verifica la conexión a la base de datos.
    
    Returns:
        bool: True si la conexión es exitosa, False en caso contrario.
    """
    try:
        with engine.connect() as connection:
            connection.execute(text("SELECT 1")) #intente hacer un select 1 en esa conexion
        return True
    except (OperationalError, DisconnectionError) as e:
        logger.error(f"Error de conexión a la base de datos: {str(e)}")
        return False

# if __name__ == "__main__":
#     resultado = check_database_connection()
#     print("¿Conexión exitosa?:", resultado)


