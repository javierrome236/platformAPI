import connexion
import six
import datetime

from swagger_server.models.device import Device  # noqa: E501
from swagger_server.models.position import Position  # noqa: E501
from swagger_server.models.statistics import Statistics  # noqa: E501
from swagger_server import util


def get_activity_statistics(user_id):  # noqa: E501
    """Devuelve las estadísticas de actividad de un usuario

     # noqa: E501

    :param user_id: id del usuario cuyas estadísticas se van consultar
    :type user_id: int

    :rtype: Statistics
    """{
  "id": 12345,
  "steps": 9999,
  "avgSteps": 5000,
  "kms": "6,8",
  "AvgKms": "3,4",
  "AvgActivity": "2,5",
  "statsDate": "1/1/2020"
}
    
    return new Statistics(user_id,9999,5000,6.8,3.4,2.5,datetime.datetime.now())


def get_live_time_position(device_id):  # noqa: E501
    """Devuelve posición actual del dispositivo

     # noqa: E501

    :param device_id: id del dispositivo del que se quiere obtener la localización
    :type device_id: int

    :rtype: Position
    """
    return 'do some magic!'


def post_device(device_id, body=None):  # noqa: E501
    """añade un nuevo dispositivo a la cuenta

     # noqa: E501

    :param device_id: id del dispositivo añadido
    :type device_id: int
    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Device.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
