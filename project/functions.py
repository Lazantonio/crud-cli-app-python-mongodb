def create_user(collection):
    '''A) Crear un usuario'''

    username = input('Username: ')
    edad = int(input('Edad: '))
    email = input('Email: ')

    user = dict(username=username, edad=edad, email=email)

    collection.insert_one(user)

    print(user)

    return user


def get_user():
    '''B) Consultar un usuario'''
    print('Obtener usuario')


def delete_user():
    '''C) Eliminar un usuario'''
    print('Eliminar usuario')


def update_user():
    '''D) Actualizar un usuario'''
    print('Actualizar usuario')


def default(*args, **kwargs):
    print('Opción no valida')
