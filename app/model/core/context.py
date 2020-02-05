import enum
from abc import ABC

from app.model.exception.exceptions import InvalidTypeException


class ContextType(enum.Enum):
    Start = 0,
    LoginSuccess = 1,
    LoginFailure = 2,
    CaptchaSuccess = 3,
    CaptchaFailure = 4

class StateType(enum.Enum):
    Login = 0,
    Captcha = 1


class ContextModel(ABC):
    def __init__(self):
        self.__error = False
        self.__result = {}
        self.__type = ContextType.Start

    @property
    def error(self):
        return self.__error

    @error.setter
    def error(self, value):
        if not isinstance(value, bool):
            raise InvalidTypeException("value should be of type boolean")
        self.__error = value

    @property
    def result(self):
        return self.__result

    @result.setter
    def result(self, value):
        if not isinstance(value, object):
            raise InvalidTypeException("value should be of type boolean")
        self.__result = value

    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, value):
        if not isinstance(value, ContextType):
            raise InvalidTypeException("value should be of type ContextType")
        self.__type = value
