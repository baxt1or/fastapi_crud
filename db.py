import os
import logging
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session, declarative_base
from collections.abc import Generator


# from dotenv import load_dotenv

# # Loading the file from a local .env file
# load_dotenv()

# Configuring the logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Instantiating the URL string
# DATABASE_URL = os.getenv("DATABASE_URL")



# Creating the engine
try:
   DATABASE_URL = "mysql+pymysql://root:ayubkot123@localhost/pythondb"

   if DATABASE_URL is None:
       raise ValueError("DATABASE url is not set.")
   
   engine = create_engine(DATABASE_URL)

except Exception as e:
    logger.error(f"Error occured while creating database {e}")
    raise

# Creating local session
SessionLocal = sessionmaker(autoflush=False, autocommit=False, bind=engine)

# Instantiating the Base
Base = declarative_base()

# Function that return db
def get_db() -> Generator[Session, None, None]:
    """ Yields database to use for context manager."""
    db = SessionLocal()
    try:

        yield db

    except Exception as e:

        logger.error(f"Error with loading database: {e}")
        db.rollback()
        raise

    finally:
        db.close()