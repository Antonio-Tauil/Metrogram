from classes.comment import Comment
from classes.like import Like
from classes.user import User
from classes.post import Post
from classes.media import Multimedia

def find_user_by_id(Users: [User], id: str) -> User:
    """
        Esta función se encarga de buscar un usuario por su id.
        Args:
            Users (list[User]): Una lista de objetos User.
            id (str): El id del usuario a buscar.
        Returns:
            User: El usuario encontrado.
    """
    for user in Users:
        if user.get_user_id() == id:
            return user

def find_user_by_username(users: [User], username : str):
    """
        Esta función se encarga de buscar un usuario por su username.
        Args:
            Users (list[User]): Una lista de objetos User.
            username (str): El username del usuario a buscar.
        Returns:
            User: El usuario encontrado.
    """
    return all(user.get_username() != username for user in users)

def find_user_by_username(users: [User], username : str):
    """
        Esta función se encarga de buscar un usuario por su username.
        Args:
            Users (list[User]): Una lista de objetos User.
            username (str): El username del usuario a buscar.
        Returns:
            User: El usuario encontrado.
    """
    for user in users:
        if user.get_username() == username:
            return user

def save_data(users: [User], posts : [Post], deleted_users : [str], deleted_posts : [(str, str)]) -> None:
    """
        Metodo que guarda la info precargada en un Txt de los posts y de los usuarios

        Args:
            users (list[User]): Lista de usuarios
            posts (list[Post]): Lista de posts

        Returns:
            None
    """
    
    with open("users.txt", "w", encoding="utf-8") as file:
        for idx,user in enumerate(users):
            if idx != len(users) -1 :
                file.write(f"{user} \n")
            else:
                file.write(f"{user}")
            #file.write(f"{user} {"\n" if idx != len(users)-1 else ''}")

    with open("followings.txt","w") as f:
        for user in users:
            for following in user.get_following():
                f.write(f"{user.get_user_id()} {following.get_user_id()}\n")

    with open("posts.txt","w", encoding="utf-8") as fs:
        for idx,post in enumerate(posts):
            if idx != len(posts) -1 :
                fs.write(f"{post} \n")
            else:
                fs.write(f"{post}")
            #fs.write(f"{post} {"\n" if idx != len(posts)-1 else ''}")

    with open("likes.txt","w") as fa:
        for post in posts:
            for like in post.get_interactions().get("likes"):
                fa.write(f"{post.get_post_id()} {like.get_user_id()}\n")

    with open("comments.txt","w", encoding="utf-8") as fq:
        for post in posts:
            for comment in post.get_interactions().get("comments"):
                # Comment(user, datetime.now().strftime("%Y-%m-%dT%H:%M:%S"), comment_content)
                fq.write(f"{post.get_post_id()}\n{comment.get_date()}\n{comment.get_comment()}\n{comment.get_user_id()}\n")

    with open("deleted_users.txt", "w") as fg:
        for deleted_user in deleted_users:
            fg.write(deleted_user)

    with open("deleted_posts.txt", "w") as ft:
        for deleted_post in deleted_posts:
            ft.write(f"{deleted_post[0]} {deleted_post[1]}")

def read_from_txt() -> list | None:
    '''
        Metodo que lee la info precargada de un txt
        se ejecutará siempre que ya exista el archivo, sino lo crea
        Returns:
            list: Lista de usuarios | None si no existe el archivo
    '''
    try:
        with open("users.txt", 'r', encoding="utf-8") as f:
            # every seven lines is a new user
            users = []
            lines = f.readlines()
            for i in range(0, len(lines), 7):
                user_id = lines[i].strip()
                name = lines[i+1].strip()
                email = lines[i+2].strip()
                username = lines[i+3].strip().replace("@","")
                _type = lines[i+4].strip()
                career = lines[i+5].strip()
                is_admin = lines[i+6].strip() == "administrador"
                user = User(user_id, name, email, username, _type, career, is_admin)
                users.append(user)

        with open("followings.txt", 'r') as fa:
            # every empty line it indicates is a new list of followings for a user
            for line in fa:
                user_id, following_id = line.strip().split(" ")
                user = find_user_by_id(users, user_id)
                following = find_user_by_id(users, following_id)
                user.follow_user(following)

        with open("posts.txt", 'r', encoding="utf-8") as fs:
            #Cada 7 lineas es un nuevo post
            # Linea 1 Id Post
            # Linea 2 Id Usuario
            posts = []
            lines = fs.readlines()
            for i in range(0, len(lines), 7):
                post_id = lines[i].strip()
                publisher_id = lines[i+1].strip()
                caption = lines[i+2].strip()
                tags = lines[i+3].strip().replace("#","").split(" ")
                date = lines[i+4].strip()
                post_type = lines[i+5].strip()
                media = lines[i+6].replace("Multimedia: ","").strip().split(" - ")
                publisher = find_user_by_id(users,publisher_id)
                _post = Post(post_id,caption,post_type,tags,date,publisher,Multimedia(media[0],media[1]))
                posts.append(_post)
                publisher.post(_post)

        with open("comments.txt", 'r', encoding="utf-8") as fq:
            #Cada 4 lineas es un nuevo comentario
            # linea 1 es el id del post
            # linea 2 es la fecha
            # linea 3 es el comentario
            # linea 4 es el id del usuario
            # En el Post <Linea 1> en la fecha <Linea 2> se Comento <Linea 3> por <Linea 4>
            lines = fq.readlines()
            for i in range(0, len(lines), 4):
                post_id = lines[i].strip()
                date = lines[i+1].strip()
                comment = lines[i+2].strip()
                user_id = lines[i+3].strip()
                user = find_user_by_id(users,user_id)
                post = next(post for post in posts if post.get_post_id() == post_id)
                post.add_comment(Comment(user,date,comment))

        with open("likes.txt","r") as fr:
            #Cada linea tiene uuid post - uuid user
            for line in fr:
                post_id, user_id = line.strip().split(" ")
                user = find_user_by_id(users,user_id)
                post = next(post for post in posts if post.get_post_id() == post_id)
                post.add_like(Like(user,post.get_date()))

        with open("deleted_users.txt", "r") as fw:
            deleted_users = list(fw)


        with open("deleted_posts.txt", "r") as fp:
            deleted_posts = []
            for line in fp:
                user_id, post_id = line.strip().split(" ")
                deleted_posts.append((user_id,post_id))

        return [users,posts, deleted_users, deleted_posts]


    except FileNotFoundError:
        print("No existe el archivo")
        return None
    
# Diccionario auxiliar para traducir las cabeceras de las tablas de informacion
aux_dict = {
    "name" : "Nombre",
    "email" : "Correo",
    "username" : "Usuario",
    "type" : "Tipo",
    "career" : "Carrera/Departamento",
    "is_admin" : "Es administrador",
    "caption" : "Descripcion",
    "tags" : "Etiquetas",
    "date" : "Fecha",
    "post_type" : "Tipo",
    "publisher" : "Publicador",
    "multimedia" : "Multimedia",
}


   
