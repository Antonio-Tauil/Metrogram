import uuid
import requests
from classes.media import Multimedia
from classes.user import User
from utils.util import find_user_by_id
from classes.post import Post

def fetch_users(url ="https://raw.githubusercontent.com/Algoritmos-y-Programacion-2223-3/api-proyecto/08d4d2ce028692d71e9f8c32ea8c29ae24efe5b1/users.json") -> list[User]:
    """
        Esta función se encarga de obtener los usuarios desde la API.
        Y los mapea a objetos User.
        Args:
            url (str): La URL de la API.
        Returns:
            list[User]: Una lista de objetos User.
    """
    users = None
    try:
    # TODO: envolver en un try catch
        response = requests.get(url).json()
        users: [User] = []

        for user in response:
            _id = user.get("id")
            name = user.get("firstName") + " " + user.get("lastName")
            email = user.get("email")
            username = user.get("username")
            _type = user.get("type")
            career = (
                user.get("department")
                if (_type == "professor")
                else user.get("major")
            )
            user = User(_id, name, email, username, _type, career)
            users.append(user)

        assign_followings(users, response)
    except requests.exceptions.JSONDecodeError:
        print("Error al cargar los usuarios, Url incorrecta")

    except requests.exceptions.ConnectionError:
        print("Error al cargar los usuarios, sin acceso a internet")

    finally:
        return users

def fetch_data(url = "https://raw.githubusercontent.com/Algoritmos-y-Programacion-2223-3/api-proyecto/08d4d2ce028692d71e9f8c32ea8c29ae24efe5b1/posts.json"):
    '''
        Metodo que obtiene los posts desde la api y los mapea a objetos Post

        Args:
            url (str): La URL de la API.

        Returns:
            [list[User]: Una lista de objetos User, list[Post]: Una lista de objetos Post.]
    '''
    posts = None
    print("Obteniendo del API")
    try:
        users = fetch_users()
        if users is None:
            return None
        response = requests.get(url).json()
        posts : list = []
        for post in response:
            publisher = post.get("publisher")
            _type = post.get("type")
            caption = post.get("caption")
            _date = post.get("date")
            tags = post.get("tags")
            multimedia = post.get("multimedia")
            multimedia_type = multimedia.get("type")
            multimedia_url = multimedia.get("url")
            multimedia = Multimedia(multimedia_type, multimedia_url)
            post = Post(uuid.uuid4(),caption,_type ,tags, _date, publisher, multimedia)
            posts.append(post)

        new_users, new_posts = assign_posts(users, posts)
    except requests.exceptions.JSONDecodeError:
        print("Error al cargar los usuarios, Url incorrecta")

    except requests.exceptions.ConnectionError:
        print("Error al cargar los usuarios, sin acceso a internet")
    finally:
        return new_users, new_posts,[],[]

def assign_followings(users: list[User], json: {}) -> None:
    '''
        Metodo que busca los usuarios que sigue cada usuario y los asigna a la lista de seguidos de cada usuario

        Args:
            users (list[User]): Lista de usuarios
            json ({}): Json con los datos de los usuarios

        Returns:
            None
    '''
    for user in users:
        for user_json in json:
            for following in user_json.get("following"):
                if user.get_user_id() == user_json.get("id"):
                    user.follow_user(find_user_by_id(users, following))

def assign_posts(users: [User], posts: [Post]) -> None:
    """
        Esta función se encarga de asignar los posts a cada usuario.

        Args:
            users (list[User]): Lista de usuarios
            posts (list[Post]): Lista de posts

        Returns:

    """
    for user in users:
        for _post in posts:
            if _post.get_publisher()==user.get_user_id():
                _post.set_publisher(user)
                user.post(_post)
    
    return [users, posts]