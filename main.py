from models.models__usuario import ModeloUsuario
from models.models__sesion import ModeloSecion

# Crear usuario
nuevo_usuario = ModeloUsuario.registrarse('andyno_9','1a$234asA')

# Iniciar sesion
iniciar_sesion = ModeloSecion('andyno_9', '1a$234asA')

# Cerrar sesion
cerrarar_sesion = iniciar_sesion.cerrar_sesion()