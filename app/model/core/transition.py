import enum
from abc import ABC, abstractmethod

from app.model.core.context import ContextModel, TransitionType
from app.model.core.state import StateModel
from app.model.exception.exceptions import InvalidTypeException
from app.service.transition.transition_builder import TransitionResponsibilityCheckerBuilder


class TransitionModel(ABC):
    def __init__(self, state,checker):
        self.state = state
        self.responsibility_checker = checker

    @property
    def state(self):
        return self.__state

    @state.setter
    def state(self, value):
        if not isinstance(value, StateModel):
            raise InvalidTypeException("value should be of type StateModel")
        self.__state = value


    def responsible(self, context):
        if not isinstance(context, ContextModel):
            raise InvalidTypeException("value should be of type ContextModel")
        return self.responsibility_checker(context.type)
