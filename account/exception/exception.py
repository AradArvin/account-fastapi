

class Error(Exception):
    pass


class UserNotFoundError(Error):
    
    def __init__(self, message: str = "User not found!") -> None:
        super().__init__(message)


