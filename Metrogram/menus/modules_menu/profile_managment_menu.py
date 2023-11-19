

from classes.post import Post
from classes.user import User
from menus.modules_menu.edit_profile_menu import edit_profile_menu
from menus.modules_menu.search_profile_menu import search_profile_menu
from utils.clear import clear

#DONE
def profile_managment_menu(user: User,users: [User]):
    clear()
    op = "-1"

    while op != "0":
        print("\t\tGestión de perfil\n")
        print("\t\t1.- Buscar perfiles")
        print("\t\t2.- Editar perfil")
        print("\t\t3.- Eliminar perfil")
        print("\t\t4.- Ver perfil")
        print("\t\t5.- Ver solicitudes se seguimiento")
        print("\t\t0.- Regresar")
        op = input("\t\tIngrese una opcion: ")

        if op == "1":
            clear()
            search_profile_menu(user, users, False)

        elif op == "2":
            clear()
            edit_profile_menu(user,users)

        elif op == "3":
            clear()
            print("\t\tEliminar perfil\n")
            decision = input("\t\tEsta seguro que desea eliminar su perfil?(s/n) ")
            while decision not in ["s","S","n","N"]:
                print("\t\tOpcion invalida")
                decision = input("\t\tEsta seguro que desea eliminar su perfil?(s/n) ")

            if decision in ["s","S"]:
                users.remove(user)
                message("\t\tPerfil eliminado con éxito!")
                user = None
                return

        elif op == "4":
            show_user(user)

        elif op == "5":
            show_follow_requests(user)

        elif op == "0":
            clear()

        else: 
            message("\t\tOpcion invalida")

    return user


def message(message : str):
    print(message)
    input("\t\tPresione enter para continuar...")
    clear()


def show_follow_requests(user: User) -> None:
    """
        Metodo que muestra las solicitudes de seguimiento indicando el nombre de usuario de la persona que quiere seguir a `user`

        Args:
            user : User que vera sus solicitudes

        Return:
            None
    """
    follow_requests = user.get_follow_requests()
    if not follow_requests:
        clear()
        print("\t\tNo tienes solicitudes de seguimiento")
        input("\t\tPresione enter para continuar...")
        clear()
        return
    clear()
    print("\t\tSolicitudes de seguimiento")
    for idx,_user in enumerate(follow_requests):
        print(f"\t\t{idx+1}.- @{_user.get_username()}")

    op = input("\t\tDesea aceptar alguna solicitud?(s/n) ")
    while op not in ["s","S","n","N"]:
        print("\t\tOpción inválida...")
        op = input("\t\tDesea aceptar alguna solicitud?(s/n) ")

    if op in ["n","N"]:
        clear()
        return

    op_to_approve = input("\t\tIndique el numero de la solicitud para aprobarla: ")
    while not op_to_approve.isdigit() or int(op_to_approve) > len(follow_requests) or int(op_to_approve) < 1:
        print("\t\tOpción inválida...")
        op_to_approve = input("\t\tIndique el numero de la solicitud para aprobarla: ")
    
    selected_user = follow_requests[int(op_to_approve)-1]

    user.accept_follow_request(selected_user)
    print(f"\t\tSolicitud de seguimiento de {selected_user.get_username()} aceptada correctamente!")
    input("\n\t\tPresione enter para continuar...")
    clear()


def show_user(user):
    clear()
    print("\t\tPerfil de usuario\n")
    print(f"\t\tNombre: {user.get_name()}")
    print(f"\t\tEmail: {user.get_email()}")
    print(f"\t\tNombre de usuario: @{user.get_username()}")
    print(f"\t\tTipo de usuario: {user.get_type()}")
    print(f"\t\t{"Carrera" if user.get_type() == "student" else "Departamento"}: {user.get_career()}")
    print("\n\t\tPublicaciones:")
    user.print_posts()
    input("\t\tPresione enter para continuar...")
    clear()