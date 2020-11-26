import connexion
import six
import pymongo

from swagger_server.models.user import User  # noqa: E501
from swagger_server import util

client = pymongo.MongoClient("mongodb+srv://test:test@cluster0.m8mga.mongodb.net/test?retryWrites=true&w=majority")
db=client.get_database('ist')


def create_user(body):  # noqa: E501
    """Crea un nuevo usuario en el sistema

     # noqa: E501

    :param body: Created user object
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = User.from_dict(connexion.request.get_json())  # noqa: E501
        collection = db.user
        user_data={
            'id': body.id,
            'username': body.username,
            'firstName': body.first_name,
            'lastName': body.last_name,
            'email': body.email,
            'password': body.password,
            'phone': body.phone
        }
        collection.insert_one(user_data)
    return 'OK'


def delete_user(username):  # noqa: E501
    """dar de baja un usuario en el sistema

     # noqa: E501

    :param username: id del usuario a borrar
    :type username: int

    :rtype: None
    """
    collection = db.user
    collection.deleteOne( { 'username': str(username) } )
    return 'OK'


def get_user_by_name(username):  # noqa: E501
    """Obtiene el usuario por el nombre de usuario

     # noqa: E501

    :param username: nombre de usuario
    :type username: str

    :rtype: User
    """
    collection = db.user
    u = collection.find_one( { 'username': str(username) } )
    return User(u['id'],u['username'],u['firstName'],u['lastName'],u['email'],u['password'],u['phone'])


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
        collection = db.user
        myquery = { "username": username }
        newvalues = { "$set": { 'id': body.id,
            'username': body.username,
            'firstName': body.first_name,
            'lastName': body.last_name,
            'email': body.email,
            'password': body.password,
            'phone': body.phone} }

        collection.update_one(myquery, newvalues)
    return 'OK'
