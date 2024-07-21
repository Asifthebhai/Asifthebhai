from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLDB = f'FastAPI\Blog\blog.db'

engine = create_engine(SQLDB,connect_args={"check_same_thread": False})

localsession = sessionmaker(bind=engine, autocommit=False, autoflush=False)

Base = declarative_base()
    