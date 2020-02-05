import enum
from abc import ABC

from app.model.core.context import TransitionType
from app.model.exception.exceptions import InvalidTypeException
from app.service.transition.transition_service import LoginSuccessTransitionResponsibilityCheckerStrategy, \
    CaptchaFailureTransitionResponsibilityCheckerStrategy, LoginFailureTransitionResponsibilityCheckerStrategy, \
    CaptchaSuccessTransitionResponsibilityCheckerStrategy, StartTransitionResponsibilityCheckerStrategy, \
    DefaultTransitionResponsibilityCheckerStrategy


class TransitionResponsibilityCheckerBuilder(ABC):

    def build(self, type):
        """

        :param type: TransitionResponsibilityCheckerType
        :return: TransitionResponsibilityCheckerStrategy
        """
        if not isinstance(type, TransitionType):
            raise InvalidTypeException("value should be in format of ContextType")
        if type == TransitionType.Start:
            return StartTransitionResponsibilityCheckerStrategy()
        if type == TransitionType.CaptchaSuccess:
            return CaptchaSuccessTransitionResponsibilityCheckerStrategy()
        if type == TransitionType.CaptchaFailure:
            return CaptchaFailureTransitionResponsibilityCheckerStrategy()
        if type == TransitionType.LoginFailure:
            return LoginFailureTransitionResponsibilityCheckerStrategy()
        if type == TransitionType.LoginSuccess:
            return LoginSuccessTransitionResponsibilityCheckerStrategy()
        if type == TransitionType.SlotOpen:
            return DefaultTransitionResponsibilityCheckerStrategy()
        if type == TransitionType.SlotClose:
            return DefaultTransitionResponsibilityCheckerStrategy()