
class User:

    def __init__(self, user_id : str, name: str, email: str, username:str, type:str,career:str,is_admin = False) -> None:
        """
            Inicializa una nueva instancia de User.

            Args:
        user_id (int): El identificador único para el usuario.
        name (str): El nombre del usuario.
        email (str): La dirección de correo electrónico del usuario.
        username (str): El nombre de usuario del usuario.
        career (str): La carrera del usuario.
        Ejemplo de uso:
        >>> user = User(1, 'Juan Perez', 'juan.perez@example.com', 'juanperez', 'Ingeniero')
        """
        self.__user_id = user_id
        self.__name = name
        self.__email = email
        self.__username = username
        self.__type = type
        self.__career = career
        self.__is_admin = is_admin
        self.__following = []
        self.__posts = []
        self.__follow_requests = []

    def get_user_id(self) -> str:
        return self.__user_id
    
    def get_name(self) -> str:
        return self.__name
    
    def get_email(self) -> str:
        return self.__email
    
    def get_username(self) -> str:
        return self.__username
    
    def get_type(self) -> str:
        return self.__type
    
    def get_career(self) -> str:
        return self.__career
    
    def get_is_admin(self) -> bool:
        return self.__is_admin
    
    def get_following(self) -> list:
        return self.__following
    
    def get_posts(self) -> list:
        return self.__posts

    def get_follow_requests(self) -> list:
        return self.__follow_requests
    
    
    def set_user_id(self, user_id) -> None:
        self.__user_id = user_id

    def set_name(self, name) -> None:
        self.__name = name

    def set_email(self, email) -> None:
        self.__email = email

    def set_username(self, username) -> None:
        self.__username = username

    def set_type(self, type) -> None:
        self.__type = type

    def set_career(self, career) -> None:
        self.__career = career

    def set_is_admin(self, is_admin) -> None:
        self.__is_admin = is_admin

    def __str__(self) -> str:
        """
            Esta función se encarga de convertir el objeto User a un string.

            Returns:
                str: El objeto User convertido a string.
        """
        return f'{self.__user_id}\n{self.__name}\n{self.__email}\n@{self.__username}\n{self.__type}\n{self.__career}\n{"administrador" if self.__is_admin else "usuario"}'
    

    def follow_user(self, user) -> None:
        """
            Esta función se encarga de seguir a un usuario.

            Args:
                user (User): El usuario a seguir.
        """
        self.__following.append(user)

    def unfollow_user(self, user) -> None:
        """
            Esta funcion se encarga de elminiar al usuario `user` de la lista de seguidos de self

            Args:
                user : User a dejar de seguir

            Returns:
                None
        """
        self.__following.remove(user)


    def accept_follow_request(self, user) -> None:
        """
            Esta funcion se encarga de aceptar la solicitud de seguimiento del usuario `User` a Self

            Args:
                user : Usuario que esta solicitando 

            Returns:
                None
        """
        self.__follow_requests.remove(user)
        user.follow_user(self)

    def register_follow_request(self, user) -> None:
        self.__follow_requests.append(user)

    def post(self, post) -> None:
        """
            Esta función se encarga de publicar un post.

            Args:
                post (Post): El post a publicar.
        """
        self.__posts.append(post)

    def print_posts(self) -> None:
        """
            Esta función se encarga de imprimir los posts del usuario.
        """
        for post in self.__posts:
            print()
            print(f"\t\tDescripción: {post.get_caption()}")
            print(f"\t\tFecha: {post.get_date()}")
            print(f"\t\tTags: {"#"+" #".join(post.get_tags())}")
            print(f"\t\tTipo de Publicación: {post.get_type()}")
            print(f"\t\tMultimedia: {post.get_multimedia()}")

