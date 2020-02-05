import enum
from abc import ABC

from app.model.exception.exceptions import InvalidTypeException


class TransitionType(enum.Enum):
    Start = 0,
    LoginSuccess = 1,
    LoginFailure = 2,
    CaptchaSuccess = 3,
    CaptchaFailure = 4,
    SlotOpen = 5,
    SlotClose = 6


class StateType(enum.Enum):
    Login = 0,
    Captcha = 1,
    Scrap = 2


class ContextModel(ABC):
    def __init__(self):
        self.__error = False
        self.__result = {}
        self.__type = TransitionType.Start

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
            raise InvalidTypeException("value should be of type object")
        self.__result = value

    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, value):
        if not isinstance(value, TransitionType):
            raise InvalidTypeException("value should be of type ContextType")
        self.__type = value
