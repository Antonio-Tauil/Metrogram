# from classes.post import Post

class Interaction:

    def __init__(self, user, date:str) -> None:
        self.__user = user
        self.__date = date

    def add_interacion (self, post) -> str:
        raise NotImplementedError("Este método debe ser implementado por las subclases")
    
    def get(self,) -> str:
        raise NotImplementedError("Este método debe ser implementado por las subclases")

    def get_user(self):
        return self.__user
    
    def get_date(self):
        return self.__date