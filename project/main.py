import functions as fn
from config import url
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

if __name__ == '__main__':

    # Crear un nuevo cliente y conectarse al servidor
    client = MongoClient(url, server_api=ServerApi('1'))

    # Acceder a la base de datos 'Anycompany'
    db = client['Anycompany']

    # Acceder a la colección 'users'
    collection = db['users']

    # Enviar un ping para confirmar una conexión exitosa
    try:
        client.admin.command('ping')
        print("Has hecho ping a tu despliegue. ¡Te has conectado exitosamente a MongoDB!")
    except Exception as e:
        print(e)

    options = {
        'a': fn.create_user,
        'b': fn.get_user,
        'c': fn.delete_user,
        'd': fn.update_user,
    }

    while True:

        for key, function in options.items():
            print(function.__doc__)

        option = input('Opción: '.lower())

        if option == 'q' or option == 'quit':
            break

        function_selected = options.get(option, fn.default)
        function_selected()