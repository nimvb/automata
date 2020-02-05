from abc import ABC, abstractmethod

from app.model.core.context import ContextModel, TransitionType
from app.model.core.state import StateModel
from app.model.exception.exceptions import InvalidTypeException
from app.service.transition.transition_builder import TransitionResponsibilityCheckerBuilder


class TransitionModel(ABC):
    def __init__(self, state,responsibility_type):
        self.state = state
        self.responsibility_type = responsibility_type

    @property
    def state(self):
        return self.__state

    @state.setter
    def state(self, value):
        if not isinstance(value, StateModel):
            raise InvalidTypeException("value should be of type StateModel")
        self.__state = value

    @property
    def responsibility_type(self):
        return self.__responsibility_type

    @responsibility_type.setter
    def responsibility_type(self, value):
        if not isinstance(value, TransitionType):
            raise InvalidTypeException("value should be of type StateModel")
        self.__responsibility_type = value

    def responsible(self, context):
        if not isinstance(context, ContextModel):
            raise InvalidTypeException("value should be of type ContextModel")
        return \
            TransitionResponsibilityCheckerBuilder() \
                .build(context.type) \
                .check_responsibility(context, self.responsibility_type)
