import enum
from abc import ABC

from app.model.core.context import TransitionType, StrategyType
from app.model.exception.exceptions import InvalidTypeException
from app.service.state.state_service import StateStrategy, LoginStateStrategy, CaptchaStateStrategy, ScrapStateStrategy


class StateStrategyBuilder(ABC):

    def build(self, type):
        """

        :param type: TransitionResponsibilityCheckerType
        :return: StateStrategy
        """
        if not isinstance(type, StrategyType):
            raise InvalidTypeException("value should be in format of StateType")
        if type == StrategyType.Login:
            return LoginStateStrategy()
        if type == StrategyType.Captcha:
            return CaptchaStateStrategy()
        if type == StrategyType.Scrap:
            return ScrapStateStrategy()
