from abc import ABC, abstractmethod

from app.model.core.context import ContextModel
from app.model.exception.exceptions import InvalidTypeException


class TransitionResponsibilityCheckerStrategy(ABC):

    def responsible(self, context,target):
        """

        :param context: ContextModel
        :return: True when it's feasible otherwise False
        """
        if not isinstance(context, ContextModel):
            raise InvalidTypeException("value should be of type ContextModel")
        return self.check_responsibility(context, target)

    @abstractmethod
    def check_responsibility(self, context, target):
        pass


class DefaultTransitionResponsibilityCheckerStrategy(TransitionResponsibilityCheckerStrategy):

    def check_responsibility(self, context, target):
        return context.type == target

class StartTransitionResponsibilityCheckerStrategy(TransitionResponsibilityCheckerStrategy):

    def check_responsibility(self, context, target):
        return context.type == target


class LoginSuccessTransitionResponsibilityCheckerStrategy(TransitionResponsibilityCheckerStrategy):

    def check_responsibility(self, context, target):
        return context.type == target


class LoginFailureTransitionResponsibilityCheckerStrategy(TransitionResponsibilityCheckerStrategy):

    def check_responsibility(self, context, target):
        return context.type == target


class CaptchaFailureTransitionResponsibilityCheckerStrategy(TransitionResponsibilityCheckerStrategy):

    def check_responsibility(self, context, target):
        return context.type == target


class CaptchaSuccessTransitionResponsibilityCheckerStrategy(TransitionResponsibilityCheckerStrategy):

    def check_responsibility(self, context, target):
        return context.type == target
