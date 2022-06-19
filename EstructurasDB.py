from sqlalchemy import create_engine, Column, ForeignKey, Integer, String, Float
from sqlalchemy.orm import scoped_session, sessionmaker, backref, relationship
from sqlalchemy.ext.declarative import declarative_base

conx = create_engine("sqlite:///data.db", convert_unicode=True)
db_session = scoped_session(sessionmaker(bind=conx))
Base = declarative_base()
Base.query = db_session.query_property()

class UnidadesTable(Base):
    __tablename__ = "Unidades"
    vehicleid = Column(Integer, primary_key = True)
    positionlatitude = Column(Float)
    positionlongitude = Column(Float)
    vehiclecurrentstatus = Column(Integer)
    idalcaldia = Column(Integer, ForeignKey('Alcaldias.idalcaldia'))  

class AlcaldiasTable(Base):
    __tablename__ = "Alcaldias"
    Nombre = Column(String, primary_key = True)
    idalcaldia = Column(Integer)
    Unidades = relationship(UnidadesTable, backref="Alcaldias")  
