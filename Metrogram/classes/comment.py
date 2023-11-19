from classes.interaction import Interaction

class Comment(Interaction):

    def __init__(self, user, timestamp: str, comment: str):
        super().__init__(user, timestamp)
        self.comment = comment

    def __str__(self) -> str:
        return f"{super().get_user().get_name()} commentó {self.comment}  - {super().get_date()}"

    def add_to_post(self, post) -> None:
        post.add_comment(self)

    def get_comment(self) -> str:
        return self.comment
    
    def get_date(self) -> str:
        return super().get_date()

    def get_user_id(self):
        return super().get_user().get_user_id()