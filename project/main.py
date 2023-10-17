# Importar las funciones personalizadas y la configuración
import functions as fn
from config import url
# Importar las clases necesarias de pymongo
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
        print("¡Te has conectado exitosamente a MongoDB!")      
    except Exception as e:
        print(e)

    # Definir las opciones del menú
    options = {
        'a': fn.create_user,
        'b': fn.get_user,
        'c': fn.delete_user,
        'd': fn.update_user,
    }

    while True:

        print("Selecciona una opción: ")
        
        # Imprimir las descripciones de las opciones del menú 
        for key, function in options.items():
            print(function.__doc__)

        # Solicitar al usuario que elija una opción
        option = input('Opción: '.lower())

        # Salir del bucle si el usuario ingresa 'q' o 'quit'
        if option == 'q' or option == 'quit':
            break

        # Obtener la función seleccionada o default    
        function_selected = options.get(option, fn.default)
        function_selected(collection)