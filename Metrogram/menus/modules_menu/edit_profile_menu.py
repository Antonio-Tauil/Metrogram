from classes.user import User
from utils.clear import clear
from utils.util import find_user_by_username

#DONE
def edit_profile_menu(user: User, users: [User]) -> None:
    '''
        Metodo que se encarga de editar el perfil del usuario

        Args:
            user (User): Usuario que se va a editar

        Returns:
            None
    '''
    _type = "carrera" if user.get_type() == "student" else "departamento"

    op = "-1"
    while op != "0":
        print("\t\tEdición de perfil\n")
        print("\t\t1.- Editar nombre")
        print("\t\t2.- Editar email")
        print("\t\t3.- Editar nombre de usuario")
        print(f"\t\t4.- Editar {_type}") 
        print("\t\t0.- Regresar")
        op = input("\t\tIngrese una opcion: ")

        if op == "1":
            name = input("\t\tNombre: ")
            user.set_name(name)
            message("\t\tNombre modificado con éxito!")

        elif op == "2":
            email = input("\t\tEmail: ")
            user.set_email(email)
            message("\t\tEmail modificado con éxito!")

        elif op == "3":
            username = input("\t\tNombre de usuario: ")
            if find_user_by_username(users, username):
                message("\t\tNombre de usuario ya existe")
            else:
                user.set_username(username)
                message("\t\tNombre de usuario modificado con éxito!")
        elif op == "4":
            career = input(f"\t\t{_type}: ")
            user.set_career(career)
            message(f"\t\t{_type} modificad{'a' if _type == 'carrera' else 'o'} con éxito!")

        elif op == "0":
            clear()

        else: 
            message("\t\tOpcion invalida")


def message(message : str) -> None:
    print(message)
    input("\t\tPresione enter para continuar...")
    clear()