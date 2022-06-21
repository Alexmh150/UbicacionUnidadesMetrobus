import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType
from EstructurasDB import UbicacionesTable, VehiculosTables, EstacionesTables

"""Se trae las estructura de las bases de datos"""

class Ubicaciones(SQLAlchemyObjectType):
    class Meta:
        model = UbicacionesTable

class Vehiculos(SQLAlchemyObjectType):
    class Meta:
        model = VehiculosTables

class Estaciones(SQLAlchemyObjectType):
    class Meta:
        model = EstacionesTables


# class UbicacionesFields:
#     id = graphene.Int()
#     vehicle_id = graphene.Int()
#     estacion_id = graphene.Int()
#     date_updated = graphene.DateTime()
#     position_latitude = graphene.Float()
#     position_longitude = graphene.Float()
#     vehicle_current_status = graphene.Int()

"""Creacion de Querys"""

class Query(graphene.ObjectType):
    get_unidades = graphene.List(Vehiculos)   
    get_alcaldias = graphene.List(Estaciones)
    coodernadas_by_unidad = graphene.List(Ubicaciones, vehicle_name=graphene.Int())
    unidades_by_alcaldia = graphene.List(Ubicaciones, alcaldia_name=graphene.String())

    @staticmethod
    def resolve_get_unidades(parent, info, **args):
        return Vehiculos.get_query(info).all()

    @staticmethod
    def resolve_get_alcaldias(parent, info, **args):
        return Estaciones.get_query(info).distinct(EstacionesTables.Alcaldia).all()
    
    @staticmethod
    def resolve_coodernadas_by_unidad(parent, info, **args):
        vehicle_name = args.get("vehicle_name")
        ubicaciones_query = Ubicaciones.get_query(info)
        return (
            ubicaciones_query.join(VehiculosTables).filter(VehiculosTables.vehicle_id.contains(vehicle_name)).all()
        )
    
    @staticmethod
    def resolve_unidades_by_alcaldia(parent, info, **args):
        alcaldia_name = args.get("alcaldia_name")
        estaciones_query = Ubicaciones.get_query(info)
        return (
            estaciones_query.join(EstacionesTables).filter(EstacionesTables.Alcaldia.contains(alcaldia_name)).all()
        )

"""Creacion de Esquema"""

schema = graphene.Schema(
    query=Query, types=[Estaciones, Ubicaciones, Vehiculos]
)