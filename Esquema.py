import graphene
from Consultas import Query
from TipoDatos import Unidades, Alcaldias


schema = graphene.Schema(
    query=Query, types=[Unidades, Alcaldias]
)