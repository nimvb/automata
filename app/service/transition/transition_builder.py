import enum
from abc import ABC

from app.model.core.context import ContextType
from app.model.exception.exceptions import InvalidTypeException
from app.service.transition.transition_service import LoginSuccessTransitionResponsibilityCheckerStrategy, \
    CaptchaFailureTransitionResponsibilityCheckerStrategy, LoginFailureTransitionResponsibilityCheckerStrategy, \
    CaptchaSuccessTransitionResponsibilityCheckerStrategy, StartTransitionResponsibilityCheckerStrategy


class TransitionResponsibilityCheckerBuilder(ABC):

    def build(self, type):
        """

        :param type: TransitionResponsibilityCheckerType
        :return: TransitionResponsibilityCheckerStrategy
        """
        if not isinstance(type, ContextType):
            raise InvalidTypeException("value should be in format of ContextType")
        if type == ContextType.Start:
            return StartTransitionResponsibilityCheckerStrategy()
        if type == ContextType.CaptchaSuccess:
            return CaptchaSuccessTransitionResponsibilityCheckerStrategy()
        if type == ContextType.CaptchaFailure:
            return CaptchaFailureTransitionResponsibilityCheckerStrategy()
        if type == ContextType.LoginFailure:
            return LoginFailureTransitionResponsibilityCheckerStrategy()
        if type == ContextType.LoginSuccess:
            return LoginSuccessTransitionResponsibilityCheckerStrategy()
