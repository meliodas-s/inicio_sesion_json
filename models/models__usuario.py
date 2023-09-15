import json

LONGITUD_MINIMA = 8

class ModeloUsuario:
    def __init__(self,id: int, usuario: str, contrasenna: str) -> None:
        self.id = id
        self.usuario = usuario
        self.contrasenna = contrasenna

    @classmethod
    def crear_usuario(cls, usuario: str, contrasenna: str):

        # Apertura de informacion necesaria
        informacion = 'data/data__informacion.json'
        usuarios = 'data/data__usuarios.json'
        with open(informacion, 'r') as f:
            data = json.load(f)
            id = data['ultimo_id'] + 1
            data['ultimo_id'] = id
            data['usuarios_registrados'] += 1

        # Actualizar ids y cantidad usuarios
        with open(informacion, 'w') as f:
            json.dump(data, f)

        # Agregar un nuevo usuario a usuarios
        nuevo_usuario = cls(id, usuario, contrasenna)
        with open(usuarios, 'r') as f:
            datos = json.load(f)

        nuevo_usuario = nuevo_usuario.crear_json()
        datos[f'{id}'] = nuevo_usuario
        
        with open(usuarios, 'w') as f:
            json.dump(datos, f, indent = 4)

        return nuevo_usuario

    @staticmethod
    def verificar_contrasenna(contrasenna: str):
        import re

        # Verificar la longitud de la contraseña
        if len(contrasenna) < LONGITUD_MINIMA:
            return False

        # Verificar si contiene al menos una letra minúscula
        if not re.search("[a-z]", contrasenna):
            return False

        # Verificar si contiene al menos una letra mayúscula
        if not re.search("[A-Z]", contrasenna):
            return False

        # Verificar si contiene al menos un número
        if not re.search("[0-9]", contrasenna):
            return False

        # Verificar si contiene al menos un carácter especial
        if not re.search("[!@#$%^&*(),.?\":{}|<>]", contrasenna):
            return False

        # Si pasa todas las comprobaciones, la contraseña es válida
        return True

    @staticmethod
    def verificar_ususario(contrasenna: str):

        # Verificar la longitud de la contraseña
        if len(contrasenna) < LONGITUD_MINIMA:
            return False

        # Si pasa todas las comprobaciones, la contraseña es válida
        return True

    @classmethod
    def registrarse(cls, usuario: str, contrasenna: str):
        if cls.verificar_ususario(usuario) and cls.verificar_contrasenna(contrasenna):
            usuario_nuevo = cls.crear_usuario(usuario, contrasenna)
            print(f"Accion: Registrar Usuario\n  Registro exitoso\n  Nuevo usuario: {usuario_nuevo['usuario']}\n  id: {usuario_nuevo['id']}")
            return usuario_nuevo
        else:
            print("Accion: Registrar Usuario\n  Registro fallido")
            return False
    
    # Metodos de lectura
    @classmethod
    def cargar_de_json(cls, archivo):
        with open(archivo, 'r') as f:
            data = json.load(f)
        return [cls(**objeto) for objeto in data]
    
    # Metodos de guardado
    def crear_json(self):
        return {
            'id': self.id,
            'usuario': self.usuario,
            'contrasenna': self.contrasenna
        }
    
    def guardar_datos(archivo: str, objetos: list):
        with open(archivo, 'w') as f:
            lista_dicts = [objeto_dict.crear_json() for objeto_dict in objetos]
            json.dump(lista_dicts, f)