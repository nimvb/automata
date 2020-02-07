from abc import ABC
from uuid import uuid4

from app.model.core.context import ContextModel, StrategyType
from app.model.exception.exceptions import InvalidTypeException
from app.service.state.state_builder import StateStrategyBuilder
from app.service.state.state_service import StateStrategy


class StateModel(ABC):
    def __init__(self, strategy):
        self.__final = False
        self.__error = False
        self.__transitions = []
        self.__name = uuid4()
        self.__strategy = None
        self.strategy = strategy

    @property
    def final(self):
        return self.__final

    @final.setter
    def final(self, value):
        if not isinstance(value, bool):
            raise InvalidTypeException("value should be of type boolean")
        self.__final = value

    @property
    def error(self):
        return self.__error

    @final.setter
    def error(self, value):
        if not isinstance(value, bool):
            raise InvalidTypeException("value should be of type boolean")
        self.__error = value

    @property
    def strategy(self):
        return self.__strategy

    @strategy.setter
    def strategy(self, value):
        if not isinstance(value, StateStrategy):
            raise InvalidTypeException("value should be of type StateStrategy")
        self.__strategy = value

    @strategy.setter
    def error(self, value):
        if not isinstance(value, StrategyType):
            raise InvalidTypeException("value should be of type StateType")
        self.__strategy = value

    @property
    def transitions(self):
        return self.__transitions

    @transitions.setter
    def error(self, value):
        if not isinstance(value, list):
            raise InvalidTypeException("value should be of type list")
        self.__transitions = value

    def next(self, context):
        if not isinstance(context, ContextModel):
            raise InvalidTypeException("value should be of type ContextModel")
        context = self.strategy.execute(context)
        candidates = list(filter(lambda transition: transition.responsible(context), self.__transitions))
        if candidates:
            candidate = candidates[0]
            return candidate.state
        return self
