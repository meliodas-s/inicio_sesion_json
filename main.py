from models.models__usuario import ModeloUsuario
from models.models__sesion import ModeloSesion

# Crear usuario
nuevo_usuario = ModeloUsuario.registrarse('andysno_9','1a$234asA')

# Iniciar sesion
iniciar_sesion = ModeloSesion('andyno_9', '1a$234asA')

# Cerrar sesion
cerrarar_sesion = iniciar_sesion.cerrar_sesion()
