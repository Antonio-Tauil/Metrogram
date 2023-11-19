
from classes.user import User
from classes.like import Like
from classes.comment import Comment
from classes.media import Multimedia

class Post:

    def __init__(self, post_id,caption:str, _type:str, tags: list[str], date : str, publisher : User, multimedia : Multimedia) -> None:
        '''
            Inicializa un objeto Post

            Args:
                caption (str): El caption del post
                _type (str): El tipo de post
                tags (list[str]): Una lista de tags
                date (str): La fecha de publicacion
                publisher (User): El usuario que publico el post
                multimedia (Multimedia): La multimedia del post

            Returns:
                Post: Un objeto Post
        '''
        self.__post_id = post_id
        self.__caption :str = caption
        self.__type : str = _type
        self.__tags : list[str] = tags
        self.__date : str = date
        self.__multimedia : Multimedia = multimedia
        self.__interactions : dict[[Like] | [Comment]] = {
            "likes" : [],
            "comments": [],
        }
        self.__publisher: User = publisher


    '''
        Getters
    '''

    def get_post_id(self) -> str:
        return self.__post_id

    def get_caption(self) -> str:
        return self.__caption
    
    def get_type(self) -> str:
        return self.__type
    
    def get_tags(self) -> str:
        return self.__tags
    
    def get_date(self) -> str:
        return self.__date
    
    def get_publisher(self) -> str:
        return self.__publisher
    
    def get_multimedia(self) -> Multimedia:
        return self.__multimedia
    
    def get_interactions(self,) -> dict:
        return self.__interactions
    
    '''
        Setters
    '''

    def set_caption(self, caption: str) -> None:
        self.__caption: str = caption
    
    def set_type(self, _type: str) -> None:
        self.__type : str = _type

    def set_tags(self, tags: list) -> None:
        self.__tags : list = tags

    def set_date(self, date : str) -> None:
        self.__date : str = date

    def set_publisher(self, publisher : User) -> None:
        self.__publisher : User = publisher

    def set_multimedia(self, multimedia : Multimedia) -> None:
        self.__multimedia : Multimedia = multimedia

    '''
        Methods
    '''

    def add_like(self, like : Like):
        '''
            Agrega un like al post
        '''
        self.__interactions["likes"].append(like)

    def add_comment(self, comment : Comment) -> None:
        '''
            Agrega un comentario al post
        '''
        self.__interactions["comments"].append(comment)

    def remove_comment(self, comment : Comment) -> None:
        """
            Elimina un comentario del post
        """
        self.__interactions.get("comments").remove(comment)


    def __str__(self) -> None:
        tags = "#" + " #".join(self.__tags)
        multimedia = self.__multimedia.__str__()
        #TODO: Fix interactions to print nicely
        return f'''{self.__post_id}\n{self.__publisher.get_user_id()}\n{self.__caption}\n{tags}\n{self.__date}\n{self.__type}\n{multimedia}'''
    
    def print_interactions(self,only_comments=False) -> None:
        """
            Metodo para imprimir en formato de tabla las interacciones

            Args:
                None

            Returns:
                None
        """
        # Se crea el encabezado
        header = ["Número","Tipo Interacción","Usuario","Fecha","Contenido"]
        interactions = self.__interactions.get("comments") if only_comments else self.__interactions.get("likes") + self.__interactions.get("comments") 

        # Se crea una lista con los datos a imprimir
        list_to_print = [header]

        list_to_print.extend([idex+1,"Me gusta" if isinstance(i, Like) else "Comentario", "@"+i.get_user().get_username(), i.get_date(), i.get_comment() if isinstance(i,Comment) else "N/A"] for idex,i in enumerate(interactions))

        # Se calcula el ancho de cada columna 
        longest_cols = [max(len(str(row[i])) for row in list_to_print) + 5 for i in range(len(list(list_to_print[0])))]

        # Se crea el formato de cada fila

        row_format = "".join(["{:>"+str(longest_col)+ "}" for longest_col in longest_cols])

        # Se imprime el encabezado
        print(f"\t\t{row_format.format(*header)}")

        # Se imprime el separador del encabezado con los datos
        print("\t\t"+" ".join(["-"* (col_width) for col_width in longest_cols]))

        # Se imprimen los datos
        for row in list_to_print[1:]:
            print(f"\t\t{row_format.format(*row)}")

        

