from sqlalchemy import Column, Integer, Float, String, DateTime
from sqlalchemy.orm import declarative_base
from config.database import db

Base = declarative_base()

class Usuario(Base):
    __tablename__ = "usuarios"

    cpf = Column(String, primary_key=True)
    nome = Column(String)
    idade = Column(Integer)
    email = Column(String)
    senha = Column(String)
    admissão = Column(DateTime)
    altura = Column(Float)
    peso = Column(Float)

    def __init__(self, cpf:str, nome: str, idade:int, email:str, senha:str, admissão:DateTime, altura:float, peso:float):
        self.cpf = cpf
        self.nome = nome
        self.idade = idade
        self.email = email
        self.senha = senha
        self.admissão = admissão
        self.altura = altura 
        self.peso = peso

Base.metadata.create_all(bind=db)