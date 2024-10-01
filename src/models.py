import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Usuario(Base):
    __tablename__ = 'usuario'
    ID_Usuario = Column (Integer, primary_key=True)
    Nombre = Column(String(250), nullable=False)
    Apellido = Column(String(250), nullable=False)
    Correo = Column(String(250), nullable=False)
    Password = Column(String(250), nullable=False)


class Planetas(Base):
    __tablename__ = 'planetas'
    ID_Planeta = Column(Integer, primary_key=True)
    Rotation_Period = Column(Integer, nullable=False)
    Orbital_Period = Column(Integer, nullable=False)
    Gravity = Column(Integer, nullable=False)


class Personajes(Base):
    __tablename__ = 'personajes'
    Id_Personajes = Column(Integer, primary_key=True)
    Birthline = Column(Integer, nullable=False)
    Gender = Column(String(250), nullable=False)
    Height= Column(Integer, nullable=False)
    Skin_color = Column(String(250), nullable=False)
    Eye_color = Column(String(250), nullable=False)
    
   
class Datos_Favoritos(Base):
    __tablename__ = 'datos_favoritos'
    id_Favoritos = Column(Integer, primary_key=True)
    user_Id = Column(Integer, ForeignKey('usuario.ID_Usuario'))
    Planeta_ID = Column(Integer, ForeignKey('planetas.ID_Planeta'))
    Personajes_Id = Column(Integer, ForeignKey('personajes.ID_Personajes'))
    usuario = relationship(Usuario)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
