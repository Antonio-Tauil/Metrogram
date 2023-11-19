from classes.user import User
from classes.post import Post
from menus.modules_menu.multimedia_managment_menu import search_posts
from menus.modules_menu.search_profile_menu import search_profile_menu
from utils.clear import clear

def interaction_managment_menu(user :User, users: [User], posts: [Post]):
    """
        Menu para manejar las interacciones entre usuarios
    """
    op = "-1"
    clear()
    while op != "0":
        print("\t\tGestión de interacciones")
        print("\t\t1.- Seguir usuarios")
        print("\t\t2.- Dejar de seguir un usuario")
        print("\t\t3.- Comentar un post")
        print("\t\t4.- Dar like a un post")
        print("\t\t5.- Eliminar comentarios de un post")
        print("\t\t0.- Volver")
        op = input("\t\tIngrese una opción: ")

        if op == "1":
            clear()
            search_profile_menu(user,users,True)
        
        elif op == "2":
            unfollow_user_menu(user)

        elif op == "3":
            search_posts(user,"",posts,users, False,True)
        
        elif op == "4":
            search_posts(user,"",posts,users,False,False)
        
        elif op == "5":
            show_my_posts(user)

        elif op == "0":
            clear()

        else:
            message("\t\tOpción inválida...")


def unfollow_user_menu(user: User) -> None:
    """
        Metodo para decidir si dejar de seguir a alguien

        Args:
            User: Usuario actual

        Returns:
            None
    """
    clear()
    if len(user.get_following()) == 0:
        input("\t\tNo estas siguiendo a nadie!")
        clear()
        return
    print("\t\tDejar de seguir usuarios")

    followings = user.get_following()
    for idx, _user in enumerate(followings):
        print(f"\t\t{idx+1}.- {_user.get_username()}")

    will_unfollow = input("\t\tDesea dejar de seguir algun usuario?(s/n)")
    while will_unfollow not in ["s","S","n","N"]:
        print("\t\tOpción inválida...")
        will_unfollow = input("\t\tDesea dejar de seguir algun usuario?(s/n)")

    if will_unfollow in  ["N", "n"]:
        clear()
        return

    op = input("\t\tSeleccione el usuario que desea dejar de seguir ")
    while not op.isdigit() or int(op) > len(followings) or int(op) < 1:
        print("\t\tOpción inválida...")
        op = input("\t\tSeleccione el usuario que desea dejar de seguir ")

    user_to_unfollow = followings[int(op)-1]

    user.unfollow_user(user_to_unfollow)
    print(f"\t\tHas dejado de seguir a {user_to_unfollow.get_username()}")
    input("\t\tPresione enter para continuar...")
    clear()
    

def show_my_posts(user: User) -> None:
    """
        Metodo que muestra mis posts y a su vez me deja entrar en uno de mis posts para moderar los comentarios que tenga

        Args:
            user : Usuario actual

        Returns:
            None
    """
    clear()
    print("\t\tMis Posts")
    my_posts = user.get_posts()
    for idx,post in enumerate(my_posts):
        tags = "#" + " #".join(post.get_tags())
        multimedia = post.get_multimedia().__str__()
        print(f"\t\t{idx+1}.-\n\t\t{post.get_caption()}\n\t\t{tags}\n\t\t{post.get_date()}\n\t\t{post.get_type()}\n\t\t{multimedia}")

    op = input("\t\tSeleccione un post: ")

    while not op.isdigit() or int(op) > len(my_posts) or int(op) < 1:
        print("\t\tOpción inválida...")
        op = input("\t\tSeleccione un post: ")

    selected_post = my_posts[int(op)-1]
    selected_post.print_interactions(True)

    _interactions = selected_post.get_interactions().get("comments")

    if not _interactions:
        print("\t\tEsta publicación no tiene comentarios")
        input("\t\tPresione enter para continuar...")
        clear()
        return

    will_delete_comment = input("\t\tDesea eliminar un comentario?(s/n) ")

    while will_delete_comment.lower() not in ["s","n"]:
        print("\t\tOpción inválida...")
        will_delete_comment = input("\t\tDesea eliminar un comentario?(s/n) ")

    if will_delete_comment == "n":
        clear()
        return
    
    comment_option = input("\t\tIndique el número del comentario que desea eliminar: ")

    while not comment_option.isdigit() or int(comment_option) > len(_interactions) or int(comment_option) < 1:
        print("\t\tOpción inválida...")
        comment_option = input("\t\tIndique el número del comentario que desea eliminar: ")

    comment_to_delete = _interactions[int(comment_option)-1]

    confirmation = input("\t\tSeguro que desea eliminar el comentario?(s/n) ")

    while confirmation.lower() not in ["s","n"]:
        print("\t\tOpción inválida...")
        confirmation = input("\t\tSeguro que desea eliminar el comentario?(s/n) ")

    if confirmation == "n":
        clear()
        return
    
    selected_post.remove_comment(comment_to_delete)
    print("\t\tComentario eliminado correctamente!")
    input("\t\tPresione enter para continuar...")
    clear()


def message(message):
    print(f"\t\t{message}")
    input("\n\t\tPresione enter para continuar...")      
    clear()