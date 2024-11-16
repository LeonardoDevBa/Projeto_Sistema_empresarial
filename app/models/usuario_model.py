from sqlalchemy import Column, Integer, Float, String, DateTime
from sqlalchemy.orm import declarative_base
from config.database import db

Base = declarative_base()

class Usuario(Base):
    __tablename__ = "usuarios"

    cpf = Column(String(11), primary_key=True)
    nome = Column(String(100))
    sobrenome = Column(String(100))
    idade = Column(Integer)
    email = Column(String(100))
    senha = Column(String(100))
    admissao = Column(DateTime)
    altura = Column(Float(5))
    peso = Column(Float(5))

    def __init__(self, cpf:str, nome: str,sobrenome: str, idade:int, email:str, senha:str, admissao:DateTime, altura:float, peso:float):
        self.cpf = cpf
        self.nome = nome
        self.sobrenome = sobrenome
        self.idade = idade
        self.email = email
        self.senha = senha
        self.admissao = admissao
        self.altura = altura 
        self.peso = peso

Base.metadata.create_all(bind=db)