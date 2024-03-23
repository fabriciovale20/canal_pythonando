from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Criando conexão
CONN = 'sqlite:///app_mobile_flet/appflet.db'

# Criando sessão
engine = create_engine(CONN, echo=True)
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

# Classe do Produto
class Produto(Base):
    __tablename__ = 'Produto'
    id = Column(Integer, primary_key=True) # ID do Produto
    titulo = Column(String(50)) # Título do Produto
    preco = Column(Float()) # Preço do Produto

Base.metadata.create_all(engine)