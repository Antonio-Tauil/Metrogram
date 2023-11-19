from classes.user import User
from classes.post import Post
from utils.clear import clear

def moderation_managment_menu(user :User, users: [User], posts: [Post], deleted_users: [str], deleted_posts : [(str,str)]) -> None:
    """
        Menu para moderar el sistema

        Args:
            user: User el usuario administrador
            users: [User] usuarios del sistema
            posts: [Post] publicaciones del sistema

        Returns:
            None
    """
    clear()
    op = "-1"

    while op != "0":
        print("\t\tModeración del sistema")
        print("\t\t1.- Eliminar un post")
        print("\t\t2.- Eliminar un comentario")
        print("\t\t3.- Eliminar un usuario")
        print("\t\t0.- Salir")
        op = input("\t\tIngrese una opción: ")

        if op == "1":
            delete_post(posts, deleted_posts)
        
        elif op == "2":
            show_all_comments(posts)

        elif op == "3":
            delete_user(users,user, posts, deleted_users)

        elif op == "0":
            clear()

        else:
            message("\t\tOpción inválida...")

def delete_user(users : [User], user : User, posts : [Post], deleted_users : [str]) -> None:
    """
        Metodo para elegir que usuario eliminar

        Args:
            users : [User] lista de usuarios

        Returns:
            None
    """
    clear()

    print("\t\tEliminar usuario")
    for idx,_user in enumerate(users):
        print(f"\t\t{idx + 1}.- {_user.get_username()}")

    will_delete = input("\t\tDesea eliminar un usuario?(s/n) ")

    while will_delete.lower() not in ["s","n"]:
        print("\t\tOpción inválida...")
        will_delete = input("\t\tDesea eliminar un usuario?(s/n) ")

    if will_delete.lower() == "n":
        clear()
        return
    
    user_option = input("\t\tIndique el número del usuario que desea eliminar: ")

    while not user_option.isdigit() or int(user_option) > len(users) or int(user_option) < 1:
        print("\t\tOpción inválida...")
        user_option = input("\t\tIndique el número del usuario que desea eliminar: ")

    selected_user = users[int(user_option)-1]

    if selected_user.get_user_id() == user.get_user_id():
        print("\t\tNo puede eliminar su propia cuenta...")
        input("\t\tPresione enter para continuar...")
        clear()
        return
    
    #search for all the posts of the user
    posts_of_the_user = [ _post for _post in posts if _post.get_publisher().get_user_id() == selected_user.get_user_id() ]

    #delete all the posts of the user
    _ = [ posts.remove(_post) for _post in posts_of_the_user ]

    deleted_users.append(f"{selected_user.get_user_id()} {selected_user.get_name()}")

    users.remove(selected_user)

    print(f"\t\tUsuario {selected_user.get_username()} eliminado correctamente!")
    input("\t\tPresione enter para continuar...")
    clear()

def show_all_comments(posts : [Post]) -> None:
    """
        Metodo para elegir que comentario eliminar

        Args:
            posts : [Post] listado de publicaciones

        Returns:
            None
    """

    def get_post_by_id(id : str) -> Post:
        return next(_post for _post in posts if _post.get_post_id() == id)

    all_comments = []
    for post in posts:
        for comment in post.get_interactions().get("comments"):
            all_comments.append((post.get_post_id(),comment))

    # Esta variable se crea para imprimir bien todos los comentarios del sistema
    auxiliar_post = Post("","","",[],"","",None)
    # se agregan todos los comentarios a la publicación auxiliar
    _ = [ _comment.add_to_post(auxiliar_post) for id,_comment in all_comments ]

    auxiliar_post.print_interactions(True)

    will_delete_comment = input("\t\tDesea eliminar un comentario?(s/n) ")

    while will_delete_comment.lower() not in ["n","s"]:
        print("\t\tOpción inválida...")
        will_delete_comment = input("\t\tDesea eliminar un comentario?(s/n) ")

    if will_delete_comment.lower() == "n":
        clear()
        return
    
    comment_option = input("\t\tIndique el número del comentario que desea eliminar: ")
    while not comment_option.isdigit() or int(comment_option) > len(all_comments) or int(comment_option) < 1:
        print("\t\tOpción inválida...")
        comment_option = input("\t\tIndique el número del comentario que desea eliminar: ")

    selected_comment = all_comments[int(comment_option)-1]

    post_of_the_comment = get_post_by_id(selected_comment[0])

    post_of_the_comment.remove_comment(selected_comment[1])

    print("\t\tComentario eliminado correctamente!")
    input("\t\tPresione enter para continuar...")
    clear()


def delete_post(posts : [Post], deleted_posts : [(str,str)]) -> None:
    """
        Metodo para elegir que post eliminar

        Args:
            posts : [Post] lista de publicaciones

        Returns:
            None
    """

    for idx,post in enumerate(posts):
        print(
            f'\t\t{idx + 1}.- {f"{post.get_caption()[:120]}..." if len(post.get_caption()) > 120 else post.get_caption()}'
        )

    will_delete = input("\t\tDesea eliminar un post?(s/n) ")
    while will_delete.lower() not in ["s","n"]:
        print("\t\tOpción inválida...")
        will_delete = input("\t\tDesea eliminar un post?(s/n) ")

    if will_delete.lower() == "n":
        clear()
        return

    post_option = input("\t\tIndique el número del post que desea eliminar: ")

    while not post_option.isdigit() or int(post_option) > len(posts) or int(post_option) < 1:
        print("\t\tOpción inválida...")
        post_option = input("\t\tIndique el número del post que desea eliminar(s/n) ")


    selected_post = posts[int(post_option)-1]

    deleted_posts.append((selected_post.get_publisher().get_user_id(), post.get_caption()[:50]))

    posts.remove(selected_post)

    print(f"\t\tPublicación {selected_post.get_caption()[:120]} eliminada correctamente!")
    input("\t\tPresione enter para continuar...")
    clear()


def message(message : str) -> None:
    """"""
    print(message)
    input("\t\tPresione enter para continuar...")
    clear()