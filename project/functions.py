import os


def clear_system(function):

    def wrap(*args, **kwargs):
        os.system('cls')
        result = function(*args, **kwargs)
        input('')
        os.system('cls')

    wrap.__doc__ = function.__doc__
    return wrap


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

    print(user)

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
        print(user)
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


def update_user():
    '''D) Actualizar un usuario'''
    print('Actualizar usuario')


def default(*args, **kwargs):
    print('Opción no valida')
