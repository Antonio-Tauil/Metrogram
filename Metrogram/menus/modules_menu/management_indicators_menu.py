from classes.interaction import Interaction
from classes.user import User
from classes.post import Post
from utils.clear import clear
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

BAD_WORDS =[
    "marico",
    "marica",
    "idiota",
    "pajuo",
    "pajua",
    "mamaguevo",
    "mamagueva",
    "guevon",
    "guevona",
]


def managment_indicators_menu(user :User, users: [User], posts: [Post], deleted_users, deleted_posts):
    """
        Menu para ver los indicadores de gestión

        Args:
            user (User): Usuario que está en sesión
            users ([User]): Lista de usuarios
            posts ([Post]): Lista de publicaciones

        Returns:
            None
    """
    clear()
    op = "-1"

    while op != "0":
        print("\t\tIndicadores de gestión\n")
        print("\t\t1.- Usuarios con mayor cantidad de publicaciones")
        print("\t\t2.- Carreras con mayor cantidad de publicaciones")
        print("\t\t3.- Publicación con mayor cantidad de interacciones")
        print("\t\t4.- Usuarios con la mayor cantidad de interacciones (dadas y enviadas)")
        print("\t\t5.- Usuarios con la mayor cantidad de posts tumbados")
        print("\t\t6.- Carreras con la mayor cantidad de comentarios inadeacuados")
        print("\t\t7.- Usuarios eliminados")
        print("\t\t0- Salir")
        op = input("\t\tIngrese una opción: ")

        if op == "1":
            users_with_more_posts(users,)

        elif op == "2":
            careers_with_more_posts(users)

        elif op == "3":
            post_with_more_interactions(posts)

        elif op == "4":
            users_with_more_interactions(users)

        elif op == "5":
            users_with_more_posts_down(users, deleted_posts)

        elif op == "6":
            careers_with_more_inadequate_comments(users)

        elif op == "7":
            _deleted_users(deleted_users)

        elif op == "0":
            clear()

def users_with_more_posts(users : [User]) -> [User]:
    """
        Retorna una lista con los usuarios que tienen más publicaciones

        Args:
            users ([User]): Lista de usuarios
            posts ([Post]): Lista de publicaciones

        Returns:
            [User]: Lista de usuarios con más publicaciones
    """
    clear()
    print("\t\tUsuarios con más publicaciones\n")

    users_copy = users[:]

    users_copy.sort(key=lambda user: len(user.get_posts()), reverse=True)

    for user in users_copy:
        print(f"\t\t{user.get_name()} cantidad de publicaciones: {len(user.get_posts())}")

    will_view_graph = input("\n\t\t¿Desea ver el gráfico? (s/n): ")

    while will_view_graph.lower() not in ["s", "n"]:
        print("\t\tOpción inválida...")
        will_view_graph = input("\n\t\t¿Desea ver el gráfico? (s/n): ")

    if will_view_graph.lower() == "s":
        # Arreglando la lista para que sea compatible con la función show_graph
        list_of_data = [
            (f"{_user.get_name()[:120]}...", len(_user.get_posts()))
            for _user in users_copy
        ]
        show_graph(list_of_data, "Usuarios con más publicaciones", "Usuario", "Cantidad de publicaciones")
        clear()
        return

    input("\n\t\tPresione enter para continuar...")
    clear()
    

def careers_with_more_posts(users : [User],) -> [str]:
    """
        Retorna una lista con las carreras que tienen más publicaciones

        Args:
            users ([User]): Lista de usuarios
            posts ([Post]): Lista de publicaciones

        Returns:
            [str]: Lista de carreras con más publicaciones
    """

    # Se crea un set con las carreras de los usuarios
    careers = {user.get_career() for user in users}
    
    # Se crea un diccionario con las carreras como llave y la cantidad de publicaciones como valor
    careers_with_posts = {career: 0 for career in careers}

    # Se recorre la lista de usuarios y se aumenta el valor de la carrera en el diccionario
    for user in users:
        careers_with_posts[user.get_career()] += len(user.get_posts())

    # Se convierte el diccionario en una lista de tuplas
    careers_with_posts = list(careers_with_posts.items())

    # Se ordena la lista de tuplas de mayor a menor
    careers_with_posts.sort(key=lambda career: career[1], reverse=True)

    clear()

    print("\t\tCarreras con más publicaciones\n")

    for career in careers_with_posts:
        print(f"\t\t{career[0]} cantidad de publicaciones: {career[1]}")

    will_view_graph = input("\n\t\t¿Desea ver el gráfico? (s/n): ")

    while will_view_graph.lower() not in ["s", "n"]:
        print("\t\tOpción inválida...")
        will_view_graph = input("\n\t\t¿Desea ver el gráfico? (s/n): ")

    if will_view_graph.lower() == "s":
        show_graph(careers_with_posts, "Carreras con más publicaciones", "Carrera", "Cantidad de publicaciones")
        clear()
        return
    
    input("\n\t\tPresione enter para continuar...")
    clear()


def post_with_more_interactions(posts : [Post]) -> [Post]:
    """
        Retorna una lista con las publicaciones que tienen más interacciones

        Args:
            posts ([Post]): Lista de publicaciones

        Returns:
            [Post]: Lista de publicaciones con más interacciones
    """ 
    clear()

    print("\t\tPublicación con más interacciones\n")

    posts_copy = posts[:]

    posts_copy.sort(key=lambda post: len(post.get_interactions().get("likes") + post.get_interactions().get("comments")), reverse=True)

    post_ = posts_copy[0]
    print(f"\t\t{post_.get_caption()[:120]} cantidad de interacciones: {len(post_.get_interactions().get("likes") + post_.get_interactions().get("comments"))}")

    will_view_graph = input("\n\t\t¿Desea ver el gráfico? (s/n): ")

    while will_view_graph.lower() not in ["s", "n"]:
        print("\t\tOpción inválida...")
        will_view_graph = input("\n\t\t¿Desea ver el gráfico? (s/n): ")

    if will_view_graph.lower() == "s":
        # Arreglando la lista para que sea compatible con la función show_graph
        list_of_data = [
            (f"{_post.get_caption()[:120]}...", len(_post.get_interactions().get("likes") + _post.get_interactions().get("comments")))
            for _post in posts_copy
        ]

        show_graph([list_of_data[0]], "Publicación con más interacciones", "Publicación", "Cantidad de interacciones", 0)
        clear()
        return


def users_with_more_interactions(users : [User]) -> [User]:
    """
        Retorna una lista con los usuarios que tienen más interacciones

        Args:
            users ([User]): Lista de usuarios

        Returns:
            [User]: Lista de usuarios con más interacciones
    """
    clear()

    print("\t\tUsuarios con más interacciones\n")
    # Esta comprension de listas agarra las interacciones de los usuarios siempre y cuando sean mas de 0 
    interactions_users = [(_user, interactions_received) for _user in users if (interactions_received := sum(len(post.get_interactions().get("likes") + post.get_interactions().get("comments")) for post in _user.get_posts())) > 0]

    interactions_users.sort(key=lambda x: x[1], reverse=True)

    for _tuple in interactions_users:
        print(f"\t\t{_tuple[0].get_name()} Interacciones : {_tuple[1]}")

    will_view = input("\t\tDesea ver el gráfico?(s/n)")

    while will_view.lower() not in ["s","n"]:
        print("\t\tOpción inválida...")
        will_view = input("\t\tDesea ver el grafico?(s/n)")

    list_of_data = [ (_tuple[0].get_name(), _tuple[1]) for _tuple in interactions_users]

    show_graph(list_of_data,"Usuarios con la mayor cantidad de interacciones", "Usuarios","Cantidad de interacciones")
    clear()

def users_with_more_posts_down(users : [User], deleted_posts : [(str,str)]) -> [User]:
    """
        Retorna una lista con los usuarios que tienen más publicaciones tumbadas

        Args:
            users ([User]): Lista de usuarios

        Returns:
            [User]: Lista de usuarios con más publicaciones tumbadas
    """
    clear()
    list_of_data = [(user.get_name(), posts_deleted) for user in users if (posts_deleted := sum(deleted_post[0] == user.get_user_id() for deleted_post in deleted_posts)) > 0]


    list_of_data.sort(key=lambda x: x[1], reverse=True)

    _ = [ print(f"\t\t{_tuple[0]} {_tuple[1]}") for _tuple in list_of_data ]

    will_view = input("\t\tDesea ver el grafico?(s/n)")

    while will_view.lower() not in ["s", "n"]:
        print("\t\tOpcion invalida...")
        will_view = input("\t\tDesea ver el grafico?(s/n)")

    if will_view == "n":
        clear()
        return
    
    show_graph(list_of_data, "Usuarios con mas posts tumbados", "Usuarios", "Cantidad de posts tumbadados")
    clear()
        

def careers_with_more_inadequate_comments(users : [User]) -> [str]:
    """
        Retorna una lista con las carreras que tienen más comentarios inadecuados

        Args:
            users ([User]): Lista de usuarios

        Returns:
            [str]: Lista de carreras con más comentarios inadecuados
    """
    clear()


    careers = {user.get_career() for user in users}
    
    # Se crea un diccionario con las carreras como llave y la cantidad de publicaciones como valor
    careers_with_posts = {career: 0 for career in careers}

    for user in users:
        for post in user.get_posts():
            for comment in post.get_interactions().get("comments"):
                if any(bad_word in comment.get_comment() for bad_word in BAD_WORDS):
                    careers_with_posts[user.get_career()] += 1

    # Se convierte el diccionario en una lista de tuplas
    careers_with_posts = list(careers_with_posts.items())

    # Se ordena la lista de tuplas de mayor a menor
    careers_with_posts.sort(key=lambda career: career[1], reverse=True)

    for career in careers_with_posts:
        print(f"\t\t{career[0]} cantidad de comentarios inadecuados: {career[1]}")

    will_view = input("\t\tDesea ver el grafico?(s/n) ")

    while will_view.lower() not in ["s","n"]:
        print("\t\tOpcion invalida")
        will_view = input("\t\tDesea ver el grafico?(s/n)")

    if will_view == "n":
        clear()
        return

    show_graph(careers_with_posts, "Carreras con mayor cantidad de comentarios inadecuados", "Carreras", "Cantidad de comentarios inadecuados")


def _deleted_users(deleted_users : [User]) -> [User]:
    """
        Retorna una lista con los usuarios eliminados

        Args:
            users ([User]): Lista de usuarios

        Returns:
            [User]: Lista de usuarios eliminados
    """
    clear()
    for deleted_user in deleted_users:
        print(f"\t\t{" ".join(deleted_user.split(" ")[1:])}")

    will_show = input("\t\tDesea ver el grafico?(s/n)")

    while will_show.lower() not in ["s","n"]:
        print("\t\tOpción inválida...")
        will_show = input("\t\tDesea ver el gráfico?(s/n)")

    if will_show == "n":
        clear()
        return
    
    deleted_copy = [ (" ".join(deleted_user.split(" ")[1:]),1) for deleted_user in deleted_users]
    
    show_graph(deleted_copy, "Usuarios eliminados", "Usuarios", "Eliminado")



def show_graph(list_of_data : [Post | User | Interaction], title, x_label,y_label, degrees = 90) -> None:
    """
        Muestra un gráfico con los datos de la lista

        Args:
            list_of_data ([Post | User | Interaction]): Lista de datos

        Returns:
            None
    """
    # La etiqueta es el primer elemento de la tupla y el valor es el segundo
    labels = [data[0] for data in list_of_data]
    values = [data[1] for data in list_of_data]

    plt.bar(labels, values)
    plt.gca().yaxis.set_major_locator(ticker.MaxNLocator(integer=True))
    plt.xticks(rotation=degrees)
    plt.xticks(fontsize=8)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)
    plt.show()