

class Multimedia:

    def __init__(self, type : str, url: str) -> None:
        self.__type : str = type
        self.__url : str = url

    def __str__(self):
        return f"Multimedia: {self.__type} - {self.__url}"