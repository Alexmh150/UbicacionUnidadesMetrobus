from sqlalchemy import create_engine, Column, ForeignKey, Integer, String, Float, DateTime
from sqlalchemy.orm import scoped_session, sessionmaker, backref, relationship
from sqlalchemy.ext.declarative import declarative_base

"""Conexion a Base de datos"""

conx = create_engine("sqlite:///data.db", convert_unicode=True)
db_session = scoped_session(sessionmaker(bind=conx))
Base = declarative_base()
Base.query = db_session.query_property()

"""Crear estructuras y conexiones internas entre Bases de Datos"""

class EstacionesTables(Base):
    __tablename__ = "Estaciones"
    estacion_id = Column(Integer, primary_key = True)                  #Es obligatorio tener primary key
    Estacion = Column(String)
    Longitud = Column(Float)
    Latitud = Column(Float)
    Alcaldia = Column(String)

class UbicacionesTable(Base):
    __tablename__ = "Ubicaciones"
    id = Column(Integer, primary_key = True)
    vehicle_id = Column(Integer, ForeignKey('Vehiculos.vehicle_id')) 
    estacion_id = Column(Integer, ForeignKey('Estaciones.estacion_id'))
    date_updated = Column(DateTime)
    position_latitude = Column(Float)
    position_longitude = Column(Float)
    vehicle_current_status = Column(Integer)
    estaciones = relationship(EstacionesTables, backref='Estaciones')   #Cascadeo de Graph    
    
class VehiculosTables(Base):
    __tablename__ = "Vehiculos"
    vehicle_id = Column(Integer, primary_key = True)
    vehicle_label = Column(Integer)
    ubicaciones = relationship(UbicacionesTable, backref='Vehiculos')   #Cascadeo de Graph