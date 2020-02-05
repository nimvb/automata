class CustomException(Exception):
    def __init__(self, message=""):
        super(CustomException, self).__init__(message)
        pass


class InvalidIndexException(Exception):
    def __init__(self, message=""):
        super(InvalidIndexException, self).__init__(message)
        pass


class InvalidTypeException(Exception):
    def __init__(self, message=""):
        super(InvalidTypeException, self).__init__(message)
        pass

