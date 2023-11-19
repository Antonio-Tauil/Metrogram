from classes.post import Post
from classes.user import User
from menus.modules_menu.interactions_managment_menu import interaction_managment_menu
from menus.modules_menu.management_indicators_menu import managment_indicators_menu
from menus.modules_menu.moderation_managment_menu import moderation_managment_menu
from menus.modules_menu.multimedia_managment_menu import multimedia_managment_menu
from menus.modules_menu.profile_managment_menu import profile_managment_menu
from utils.clear import clear


def modules_menu(user : User, users: [User], posts: [Post], deleted_users : [str], deleted_posts : [(str,str)]):
    is_admin = user.get_is_admin()
    op ="-1"

    while op != "0":
        print("\t\tMenu Principal\n")
        print("\t\t1.- Gestión de perfil")
        print("\t\t2.- Gestión de multimedia")
        print("\t\t3.- Gestión de interacciones")
        print("\t\t4.- Gestión de moderación") if is_admin else None
        print(f"\t\t{'5.- ' if is_admin else '4.- '}Inidicadores de gestión")
        print("\t\t0.- Cerrar sesión")
        op = input("\t\tIngrese una opcion: ")

        if op == "1":
            updated_user = profile_managment_menu(user, users)
            if updated_user is None:
                return

        elif op == "2":
            multimedia_managment_menu(user, users, posts)

        elif op == "3":
            interaction_managment_menu(user, users, posts)

        elif op == "4" and is_admin:
            moderation_managment_menu(user, users, posts, deleted_users, deleted_posts)

        elif op == "4":
            managment_indicators_menu(user, users, posts, deleted_users, deleted_posts)

        elif op == "5" and is_admin:
            managment_indicators_menu(user, users, posts, deleted_users, deleted_posts)

        elif op == "0":
            alert("\t\tSesión cerrada")
        else:
            alert("\t\tOpcion invalida")
    clear()


def alert(message : str) -> None:
    print(message)
    input("\t\tPresione enter para continuar...")
    clear()