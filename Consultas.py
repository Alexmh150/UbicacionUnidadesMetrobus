import graphene
from EstructurasDB import  AlcaldiasTable, UnidadesTable
from TipoDatos import  Unidades, Alcaldias


class Query(graphene.ObjectType):
    get_unidades = graphene.List(Unidades)   
    get_alcaldias = graphene.List(Alcaldias)
    coodernadas_by_unidad = graphene.List(Unidades, vehicleid=graphene.Int())
    unidades_by_alcaldia = graphene.List(Alcaldias, Nombre=graphene.String())

    @staticmethod
    def resolve_get_unidades(parent, info, **args):
        return Unidades.get_query(info).all()

    @staticmethod
    def resolve_get_alcaldias(parent, info, **args):
        return Alcaldias.get_query(info).all()
    
    @staticmethod
    def resolve_coodernadas_by_unidad(parent, info, **args):
        vehicleid = args.get("vehicleid")
        vehicleid_query = Unidades.get_query(info)
        return vehicleid_query.filter(UnidadesTable.vehicleid.contains(vehicleid)).all()
    
    @staticmethod
    def resolve_unidades_by_alcaldia(parent, info, **args):
        Nombre = args.get("Nombre")
        unidades_query = Alcaldias.get_query(info)
        return (
            unidades_query.join(AlcaldiasTable).filter(Alcaldias.Nombre == Nombre).all()
        )