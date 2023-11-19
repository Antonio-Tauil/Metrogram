from classes.user import User
from utils.clear import clear
from utils.util import find_user_by_username

def login(users: list) -> User | None:
    '''
        Metodo que se encarga de hacer el login de un usuario

        Args:
            users (list[User]): Lista de usuarios

        Returns:
            User: Usuario logeado
    '''
    clear()
    print("\t\tInicio de sesión\n")
    username = input("\t\tNombre de usuario: ")

    if user:= find_user_by_username(users, username):
        clear()
        return user
    
    print("\t\tCredenciales invalidas")
    input("\t\tPresione enter para continuar...")
    clear()
    return None
    
