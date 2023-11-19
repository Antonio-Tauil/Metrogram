from classes.interaction import Interaction

class Like(Interaction):

    def __init__(self, user, timestamp: str):
        super().__init__(user, timestamp)

    def __str__(self) -> str:
        return f"{super().get_user().get_name()} le dió me gusta - {super().get_date()}"

    def add_to_post(self, post) -> bool:
        """
            Metodo que agrega el like al post

            Args:
                self: Like
                post: Publicacion a la que se le dara like
            Return:
                Boolean: True si se pudo agregar el Like, False si ya existia el like y se elimina el Like
        """
        
        for _like in post.get_interactions().get("likes"):
            if _like.get_user_id() == self.get_user_id():
                # Si ya le di like lo elimino
                post.get_interactions().get("likes").remove(_like)
                return False
        # Si en todos los likes del post no esta mi like entonces lo agrego
        post.add_like(self)
        return True

    def get_user_id(self):
        return super().get_user().get_user_id()
    
    