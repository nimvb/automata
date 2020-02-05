import enum
from abc import ABC

from app.model.core.context import TransitionType, StateType
from app.model.exception.exceptions import InvalidTypeException
from app.service.state.state_service import LoginStateStrategy, CaptchaStateStrategy, ScrapStateStrategy


class StateStrategyBuilder(ABC):

    def build(self, type):
        """

        :param type: TransitionResponsibilityCheckerType
        :return: TransitionResponsibilityCheckerStrategy
        """
        if not isinstance(type, StateType):
            raise InvalidTypeException("value should be in format of StateType")
        if type == StateType.Login:
            return LoginStateStrategy()
        if type == StateType.Captcha:
            return CaptchaStateStrategy()
        if type == StateType.Scrap:
            return ScrapStateStrategy()
