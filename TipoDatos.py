import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType
from EstructurasDB import UnidadesTable, AlcaldiasTable

class Unidades(SQLAlchemyObjectType):
    class Meta:
        model = UnidadesTable

class UnidadesFields:
    vehicleid = graphene.Int()
    positionlatitude = graphene.Float()
    positionlongitude = graphene.Float()
    vehiclecurrentstatus = graphene.Int()
    idalcaldia = graphene.Int()

class Alcaldias(SQLAlchemyObjectType):
    class Meta:
        model = AlcaldiasTable

# class AlcaldiasFields:
#     id = graphene.Int()
#     Nombre = graphene.String()
#     id_alcaldia = graphene.Int()