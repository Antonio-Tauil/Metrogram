from datetime import datetime
import uuid
from classes.comment import Comment
from classes.interaction import Interaction
from classes.like import Like
from classes.media import Multimedia
from classes.post import Post
from classes.user import User
from utils.clear import clear

def multimedia_managment_menu(user: User, users : [User], posts : [Post]) -> None:
    """
        Metodo que se encarga de mostrar el menu de gestión de multimedia

        Args:
            user (User): Usuario actual
            users ([User]): Lista de usuarios
            posts ([Post]): Lista de publicaciones

        Returns:
            None
    """
    clear()
    op = "-1"

    while op != "0":
        print("\t\tGestión de multimedia\n")
        print("\t\t1. Publicar Post")
        print("\t\t2. Buscar publicaciones")
        print("\t\t0.- Salir")
        op = input("\t\tIngrese una opción: ")

        if op == "1":
            clear()
            register_post(user, posts)
            message("\t\tPublicación registrada con éxito!")

        elif op == "2":
            clear()
            search_posts_menu(user, users, posts)

        elif op == "0":
            clear()

        else:
            message("\t\tOpción invalida")

#DONE
def register_post(user: User, posts: [Post]) -> None:
    """
        Metodo que se encarga de registrar una publicacion

        Args:
            user (User): Usuario actual
            posts ([Post]): Lista de publicaciones

        Returns:
            None
    """
    print("\t\tRegistro de publicación\n")
    caption = input("\t\tIngrese la descripción: ")
    _type = input("\t\tIngrese el tipo de publicación (1. Foto, 2. Video): ")
    while _type not in ['1','2']:
        print("\t\tTipo de publicación invalido")
        _type = input("\t\tIngrese el tipo de publicación (1. Foto, 2. Video): ")
    
    _type = "photo" if _type == '1' else "video"

    url = input("\t\tIngrese la url de la multimedia: ")

    media = Multimedia(_type, url)

    tags = input("\t\tIngrese los tags separados por espacio en blanco ( ): ").split(" ")

    date = datetime.now().strftime("%Y-%m-%dT%H:%M:%S")

    post = Post(uuid.uuid4(),caption, _type, tags, date, user, media)
    posts.append(post)
    user.post(post)

def search_posts_menu(user : User, users: [User], posts: [Post]) -> None:
    """
        Metodo que se encarga de buscar publicaciones

        Args:
            user (User): Usuario actual
            users ([User]): Lista de usuarios
            posts ([Post]): Lista de publicaciones

        Returns:
            None
    """
    print("\t\tBusqueda de publicaciones\n")
    op = "-1"

    while op != "0":
        print("\t\t1. Buscar por nombre usuario")
        print("\t\t2. Buscar por hashtag (#)")
        print("\t\t0. Regresar")
        op = input("\t\tIngrese una opción: ")

        if op == "1":
            clear()
            username = input("\t\tIngrese el nombre de usuario: ")
            search_posts(user, username, posts, users,False, True)

        elif op == "2":
            clear()
            hashtag = input("\t\tIngrese el Hashtag (#ejemploABuscar): ")
            search_posts(user, hashtag, posts, users,True, True)

        elif op == "0":
            clear()

        else:
            message("\t\tOpción invalida")

def show_posts(user : User, filtered_posts: [Post], user_will_comment : bool) -> None:
    """
        Metodo que se encarga de mostrar los posts

        Args:
            posts : [Post] Lista de Posts a mostrar

        Returns:
            None
    """
    clear()
    if not filtered_posts:
        message("\t\tNo se encontraron resultados")
        return

    for idx,post in enumerate(filtered_posts):
        tags = "\t\t#"+" #".join(post.get_tags())
        print(
            f'\t\t{idx + 1}.-{f"{post.get_caption()[:50]}..." if len(post.get_caption()) > 50 else post.get_caption()}\n{tags} - @{post.get_publisher().get_username()}'
        )

    op = input("\t\tDesea ver algun post?(s/n) ")
    while op not in ["s","S","n","N"]:
        print("\t\tOpción inválida...")
        op = input("\t\tDesea ver algun post?(s/n) ")

    if op in ["n", "N"]:
        clear()
        return

    new_op = input("\t\tIndique el número del Post: ")

    while not new_op.isdigit() or int(new_op) > len(filtered_posts) or int(new_op) < 1:
        print("\t\tOpción inválida...")
        new_op = input("\t\tIndique el número del Post: ")

    post = filtered_posts[int(new_op)-1]
    clear()
    #TODO: Imprimir bien el Post
    print(f"\t\tCaption:{post.get_caption()}\n\t\tTags:{'#'+' #'.join(post.get_tags())}\n\t\tFecha:{post.get_date()}\n\t\tTipo:{post.get_type()}\n\t\t{post.get_multimedia()}\n\t\tAutor: @{post.get_publisher().get_username()}")

    post.print_interactions()
    
    if user_will_comment:

        will_comment = input("\t\tDesea comentar?(s/n) ")

        while will_comment not in ["s","S","n","N"]:
            print("\t\tOpción no válida..")
            will_comment = input("\t\tDesea comentar?(s/n) ")

        if will_comment in ["n","N"]:
            redirect_to_user_profile(post.get_interactions())
            clear()
            return

        comment_content = input("\t\tIngrese el comentario: ")

        _comment = Comment(user, datetime.now().strftime("%Y-%m-%dT%H:%M:%S"), comment_content)

        _comment.add_to_post(post)

        input("\t\tComentario agregado con éxito!\n\t\tPresione enter para continuar...")
        redirect_to_user_profile(post.get_interactions())
    
    else:
        will_like = input("\t\tDesea dejar un like?(s/n)")
        while will_like not in ["s","S","n","N"]:
            print("\t\tOpción inválida...")
            will_like = input("\t\tDesea dejar un like?(s/n)")
        
        if will_like in ["n", "N"]:
            redirect_to_user_profile(post.get_interactions())
            clear()
            return
        
        _like = Like(user, datetime.now().strftime("%Y-%m-%dT%H:%M:%S"))

        could_register_like = _like.add_to_post(post)
        input(f"\t\t{'Like agregado con éxito!' if could_register_like else 'Like eliminado correctamente!'}\n\t\tPresione enter para continuar...")
        redirect_to_user_profile(post.get_interactions())
        

    clear()

def search_posts(user : User, _filter: str, posts: [Post], users: [User], is_search_by_hastag, will_comment) -> None:
    """
        Metodo que se encarga de buscar publicaciones

        Args:
            text (str): Texto a buscar
            posts ([Post]): Lista de publicaciones

        Returns:
            None
    """
    '''
        for following in user.get_following():
            for post in posts:
                if post.get_publisher().get_user_id() == following.get_user_id():
                    filtered_posts.append(post)

    '''
    # Primero filtro los posts a solo la gente que sigo
    filtered_posts = [ post for post in posts for following in user.get_following() if post.get_publisher().get_user_id() == following.get_user_id() ]

    results = []

    if is_search_by_hastag:
        # Comprension de set para filtrar los posts para buscar si existe un post que contenga el hashtag de uno de los posts de las personas que `user` sigue
        results = {
            post
            for post in filtered_posts
            for tag in post.get_tags()
            if _filter in f"#{tag}"
        }

    else:
        # Obtengo todos mis seguidos
        followings = user.get_following()
        # Obtengo todos los usuarios que hacen match con el `_filter` que en este caso es el nombre de usuario
        matching_usernames = [ following for following in followings if _filter.lower() in following.get_username().lower() ]
        # Una vez tengo los usuarios que hacen match con el `_filter` busco entre todos los posts cuando estos coinciden
        results = [ post for post in posts for _following in matching_usernames if post.get_publisher().get_user_id() == _following.get_user_id() ]


    show_posts(user, results, will_comment)

def redirect_to_user_profile(interactions: dict) -> None:
    """
        Funcion que permite redireccionar al perfil de un usuario cuando se selecciona desde el listado de likes y comentarios de un post 

        Args:
            interactions
        
        Returns:
            None
    """
    op = input("\t\tDesea ver el perfil de alguno de los usuarios?(s/n) ")
    while op.lower() not in ['s','n']:
        print("\t\tOpción inválida...") 
        op = input("\t\tDesea ver el perfil de alguno de los usuarios?(s/n) ")

    if op == "n":
        return
    if not interactions:
        message("\t\t No se encontraron resultados")
    
    op2 = input("\t\tIndique el numero de la interacción para ver el perfil del usuario que la realizó: ")
    interactions = [ interactions[key] for key in interactions.keys()]
    while not op2.isdigit() or int(op2) > len(interactions) or int(op2) < 1:
        print("\t\tOpción inválida...")
        op2 = input("\t\tIndique el numero de la interacción para ver el perfil del usuario que la realizó: ")

    try:
        user_profile = interactions[int(op2)-1][0].get_user()
        print("\n\t\tPerfil de usuario\n")
        print(f"\t\tNombre: {user_profile.get_name()}")
        print(f"\t\tEmail: {user_profile.get_email()}")
        print(f"\t\tNombre de usuario: @{user_profile.get_username()}")
        print(f"\t\tTipo de usuario: {user_profile.get_type()}")
        print(f"\t\t{'Carrera' if user_profile.get_type() == 'student' else 'Departamento'}: {user_profile.get_career()}")
        print("\n\t\tPublicaciones:")
        user_profile.print_posts()
    except:
        message("\t\tNo se encontraron resultados")
        return
    
    

def message(message : str) -> None:
    """
        Metodo que se encarga de mostrar un mensaje

        Args:
            message (str): Mensaje a mostrar

        Returns:
            None
    """
    print(message)
    input("\t\tPresione enter para continuar...")
    clear()
