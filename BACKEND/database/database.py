from sqlalchemy import create_engine

from sqlalchemy.orm import sessionmaker, declarative_base


engine=create_engine("sqlite:///./database.db", connect_args={'check_same_thread': False})


Base=declarative_base()


SessionLocal=sessionmaker(autocommit=False, autoflush=False, bind=engine)






