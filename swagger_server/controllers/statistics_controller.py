import connexion
import six
import datetime
import pymongo
import requests

from swagger_server.models.device import Device  # noqa: E501
from swagger_server.models.position import Position  # noqa: E501
from swagger_server.models.statistics import Statistics  # noqa: E501
from swagger_server import util

client = pymongo.MongoClient("mongodb+srv://test:test@cluster0.m8mga.mongodb.net/test?retryWrites=true&w=majority")
db=client.get_database('ist')



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
    time = requests.get('https://stickapi-jaime.herokuapp.com/JaimeAlvarado/Stick/1.0.0/inactivity?idDevice=23')
    time = time.json()['message']
    steps = requests.get('https://stickapi-jaime.herokuapp.com/JaimeAlvarado/Stick/1.0.0/steps?idDevice=22')
    steps = steps.json()['message']
    return Statistics(user_id,steps,5000,6.8,3.4,time,datetime.datetime.now())


def get_live_time_position(device_id):  # noqa: E501
    """Devuelve posición actual del dispositivo

     # noqa: E501

    :param device_id: id del dispositivo del que se quiere obtener la localización
    :type device_id: int

    :rtype: Position
    """
    position = requests.get('https://wristbandapi-jaime.herokuapp.com/JaimeAlvarado/WristBand/1.0.0/localization?idWrist=4')
    position = position.json()['message'].split(',')
    return Position(device_id,position[0],position[1],datetime.datetime.now())


def post_device(body=None):  # noqa: E501
    """añade un nuevo dispositivo a la cuenta

     # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: None
    """

    if connexion.request.is_json:
        body = Device.from_dict(connexion.request.get_json())  # noqa: E501
        collection = db.devices
        device_data={
            'name': body.name,
            'model': body.model
        }
        collection.insert_one(device_data)
    return 'OK'
