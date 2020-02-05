from abc import ABC, abstractmethod

from app.model.core.context import ContextModel, ContextType
from app.model.exception.exceptions import InvalidTypeException


class StateStrategy(ABC):

    def execute(self, context):
        """

        :param context: ContextModel
        :return: context
        """
        if not isinstance(context, ContextModel):
            raise InvalidTypeException("value should be of type ContextModel")
        return self.execute_strategy(context)

    @abstractmethod
    def execute_strategy(self, context):
        pass


class LoginStateStrategy(StateStrategy):
    def execute_strategy(self, context):
        print("Login strategy")
        return context


class CaptchaStateStrategy(StateStrategy):

    def execute_strategy(self, context):
        print("Captcha strategy")
        return context
