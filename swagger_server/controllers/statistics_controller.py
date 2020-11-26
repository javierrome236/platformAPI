import connexion
import six
import datetime
import pymongo

from swagger_server.models.device import Device  # noqa: E501
from swagger_server.models.position import Position  # noqa: E501
from swagger_server.models.statistics import Statistics  # noqa: E501
from swagger_server import util

client = pymongo.MongoClient("mongodb+srv://test:test@cluster0.m8mga.mongodb.net/test?retryWrites=true&w=majority")
db=client.get_database('prueba')
lol = db.pru


def delete_device(device_id):  # noqa: E501
    """borra un dispositivo de la cuenta

     # noqa: E501

    :param device_id: id del dispositivo a borrar
    :type device_id: int

    :rtype: None
    """
    return 'OK'


def get_activity_statistics(user_id):  # noqa: E501
    """Devuelve las estadísticas de actividad de un usuario

     # noqa: E501

    :param user_id: id del usuario cuyas estadísticas se van consultar
    :type user_id: int

    :rtype: Statistics
    """
    return Statistics(user_id,9999,5000,6.8,3.4,2.5,datetime.datetime.now())


def get_live_time_position(device_id):  # noqa: E501
    """Devuelve posición actual del dispositivo

     # noqa: E501

    :param device_id: id del dispositivo del que se quiere obtener la localización
    :type device_id: int

    :rtype: Position
    """
    return Position(device_id,"39.4787526","-6.3422524",datetime.datetime.now())


def post_device(body=None):  # noqa: E501
    """añade un nuevo dispositivo a la cuenta

     # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: None
    """

    if connexion.request.is_json:
        body = Device.from_dict(connexion.request.get_json())  # noqa: E501
        dev = Device.from_dict(connexion.request.get_json()
        codification_data={
            'person_id': dev.name,
            'codification': 125
        }
        lol.insert_one(codification_data)
    return 'OK'
