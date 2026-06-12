from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base,sessionmaker
engin = create_engine(
    url="sqlite:///./database_v1.db",
    connect_args={"check_same_thread":False}
)
sessionLocal = sessionmaker(
    bind=engin,
    autocommit=False,
    autoflush=False
)

base = declarative_base()

