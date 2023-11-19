from utils.clear import clear # Uso de la funcion clear
from utils.util import find_user_by_username # Uso de la funcion find_user_by_username
from classes.user import User # Uso de la clase User
import uuid # Para generar un id unico

#DONE
def register(users: list) -> User:
    """
        Metodo que se encarga de registrar un usuario

        Args:
            users (list[User]): Lista de usuarios

        Returns:
            User: Usuario registrado
    """
    clear()
    print("\t\tRegistro de usuario\n")
    name = input("\t\tNombre: ")
    lastName = input("\t\tApellido: ")
    email = input("\t\tEmail: ")

    username = input("\t\tNombre de usuario: ")
    while find_user_by_username(users, username):
        print("\t\tNombre de usuario ya existe")
        username = input("\t\tNombre de usuario: ")

    _type = input("\t\tTipo de usuario (1. Estudiante, 2. Profesor): ")
    while _type not in ['1','2']:
        print("\t\tTipo de usuario invalido")
        _type = input("\t\tTipo de usuario (1. Estudiante, 2. Profesor): ")

    _type = "student" if _type == '1' else "professor"
    
    career = input("\t\tCarrera: ") if _type == "student" else input("\t\tDepartamento: ")
    new_user = User(str(uuid.uuid4()),f"{name} {lastName}", email, username, _type, career, True)
    users.append(new_user)

    print("\t\tUsuario registrado con éxito!")
    input("\t\tPresione enter para continuar...")
    clear()

    return new_user
    