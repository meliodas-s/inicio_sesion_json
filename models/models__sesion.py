"""
Para acceder a informacion importante de cada usuario
"""

KEY_PARA_CONTRASENA = 'contrasenna'
KEY_PARA_USUARIO = 'usuario'
class ModeloSesion:
    """
    [Descripción]:
        El ModeloSesion, permite administrar las acciones del usuario
        acciones como: Editar Perfil, Cerrar sesion.
    """
    def __init__(self, usuario, contrasenna) -> None:
        self.usuario = usuario
        self.contrasenna = contrasenna

        # Iniciamos la autentificacion. Si estado True: secion activa
        self.estado = self.verificar_contrasenna()

    def verificar_contrasenna(self):
        # Accedemos a la base de datos json
        import json
        ubicacion = './data/data__usuarios.json'
        with open(ubicacion, 'r') as f:
            data = json.load(f)

        # verificamos que el usuario exista
        for key in data.keys():
            username = data[key][KEY_PARA_USUARIO]
            if (username == self.usuario):
                usuario = data[key]
                print(f"Usuario: {username}")
                print(f'Contrasenna: {usuario[KEY_PARA_CONTRASENA]}')

                # Verificamos que la contraseña sea la correctas
                if (usuario[KEY_PARA_CONTRASENA] == self.contrasenna):
                    print(f"Inicio de sesion exitoso: Usuario {username}")
                    return True
                else:
                    print(f"Inicio de sesion fallido: Usuario {username}")
                    return False

        else:
            print(f"No existe tal usuario")
            return False

    def cerrar_sesion(self):
        # Cerramos secion, estado = False
        print("Se cerro sesion")
        self.estado = False
        del self