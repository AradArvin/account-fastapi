# Basic exceptions to handle any errors that may occur.

class Error(Exception):
    pass


class UserNotFoundError(Error):
    
    def __init__(self, message: str = "User not found!") -> None:
        super().__init__(message)


class NoDataEnteredError(Error):
    
    def __init__(self, message: str = "No data entered!") -> None:
        super().__init__(message)


class UserNotLoggedInError(Error):
    
    def __init__(self, message: str = "User not logged in!") -> None:
        super().__init__(message)
