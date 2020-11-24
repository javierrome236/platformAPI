import connexion
import six

from swagger_server.models.user import User  # noqa: E501
from swagger_server import util


def create_user(body):  # noqa: E501
    """Crea un nuevo usuario en el sistema

     # noqa: E501

    :param body: Created user object
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = User.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def delete_user(username):  # noqa: E501
    """dar de baja un usuario en el sistema

     # noqa: E501

    :param username: id del usuario a borrar
    :type username: int

    :rtype: None
    """
    return 'do some magic!'


def get_user_by_name(username):  # noqa: E501
    """Obtiene el usuario por el nombre de usuario

     # noqa: E501

    :param username: nombre de usuario
    :type username: str

    :rtype: User
    """
    return 'do some magic!'


def update_user(body, username):  # noqa: E501
    """Actualiza los datos del usuario

     # noqa: E501

    :param body: Usuario actualizado
    :type body: dict | bytes
    :param username: nombre del usuario que va a ser actualizado
    :type username: str

    :rtype: None
    """
    if connexion.request.is_json:
        body = User.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
