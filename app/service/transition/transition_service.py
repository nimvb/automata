from abc import ABC, abstractmethod

from app.model.core.context import ContextModel
from app.model.exception.exceptions import InvalidTypeException


class TransitionResponsibilityCheckerStrategy(ABC):

    def responsible(self, context):
        """

        :param context: ContextModel
        :return: True when it's feasible otherwise False
        """
        if not isinstance(context, ContextModel):
            raise InvalidTypeException("value should be of type ContextModel")
        return self.check_responsibility(context)

    @abstractmethod
    def check_responsibility(self, context):
        pass


class StartTransitionResponsibilityCheckerStrategy(TransitionResponsibilityCheckerStrategy):

    def check_responsibility(self, context):
        return True


class LoginSuccessTransitionResponsibilityCheckerStrategy(TransitionResponsibilityCheckerStrategy):

    def check_responsibility(self, context):
        return True


class LoginFailureTransitionResponsibilityCheckerStrategy(TransitionResponsibilityCheckerStrategy):

    def check_responsibility(self, context):
        return True


class CaptchaFailureTransitionResponsibilityCheckerStrategy(TransitionResponsibilityCheckerStrategy):

    def check_responsibility(self, context):
        return True


class CaptchaSuccessTransitionResponsibilityCheckerStrategy(TransitionResponsibilityCheckerStrategy):

    def check_responsibility(self, context):
        return True
