import os
import pprint


def clear_system(function):

    def wrap(*args, **kwargs):
        os.system('cls')
        result = function(*args, **kwargs)
        input('')
        os.system('cls')

    wrap.__doc__ = function.__doc__
    return wrap


def show_user(user):
    pp = pprint.PrettyPrinter(indent=4)

    pp.pprint(user)


@clear_system
def create_user(collection):
    '''A) Crear un usuario'''

    username = input('Username: ')
    edad = int(input('Edad: '))
    email = input('Email: ')

    user = dict(username=username, edad=edad, email=email)

    direccion = input('¿Desea ingresar su dirección? (S/N)): ').lower()

    if direccion == 's':
        user['direccion'] = get_address()

    collection.insert_one(user)

    show_user(user)

    return user


def get_address():
    calle = input('Calle: ')
    ciudad = input('Ciudad: ')
    estado = input('Estado: ')
    codigo_postal = input('Código Postal: ')

    direccion = dict(calle=calle,
                    ciudad=ciudad,
                    estado=estado,
                    codigo_postal=codigo_postal
                    )

    return direccion


@clear_system
def get_user(collection):
    '''B) Consultar un usuario'''
    username = input('Username: ')
    user = collection.find_one(
        {'username': username},
        {'_id': False}
    )

    if user:
        show_user(user)
        return user
    else:
        print('Usuario no encontrado')


@clear_system
def delete_user(collection):
    '''C) Eliminar un usuario'''
    username = input('Username: ')

    return collection.delete_one(
        {'username': username}
    )


@clear_system
def update_user(collection):
    '''D) Actualizar un usuario'''
    username = input('Username: ')
    user = collection.find_one({'username': username})

    if user:
        print("Usuario encontrado, ingrese los nuevos datos (deje en blanco para mantener los actuales):")
        new_username = input('Nuevo Username: ')
        new_edad = input('Nueva Edad: ')
        new_email = input('Nuevo Email: ')

        if new_username:
            user['username'] = new_username
        if new_edad:
            user['edad'] = int(new_edad)
        if new_email:
            user['email'] = new_email

        direccion = input('¿Desea actualizar su dirección? (S/N)): ').lower()
        if direccion == 's':
            user['direccion'] = get_address()

        collection.update_one({'username': username}, {"$set": user})
        print("Usuario actualizado con éxito.")
    else:
        print('Usuario no encontrado')


def default(*args, **kwargs):
    print('Opción no valida')
