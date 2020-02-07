import json

from app.model.core.context import ContextModel, TransitionType, StrategyType, AnotherTransitionType
from app.model.core.state import StateModel
from app.model.core.transition import TransitionModel
from app.service.state.state_builder import StateStrategyBuilder


def entry():
    login_strategy = StateStrategyBuilder().build(StrategyType.Login)
    captcha_strategy = StateStrategyBuilder().build(StrategyType.Captcha)
    scrap_strategy = StateStrategyBuilder().build(StrategyType.Scrap)
    state_a = StateModel(login_strategy)
    state_b = StateModel(captcha_strategy)
    state_c = StateModel(scrap_strategy)
    transition_a_b = TransitionModel(state_b, lambda x: x == AnotherTransitionType.AnotherLoginSuccess)
    transition_b_a = TransitionModel(state_a, lambda x: x == AnotherTransitionType.AnotherCaptchaFailure)
    transition_b_c = TransitionModel(state_c, lambda x: x == AnotherTransitionType.AnotherCaptchaSuccess)
    state_a.transitions.append(transition_a_b)
    state_b.transitions.append(transition_b_a)
    state_b.transitions.append(transition_b_c)

    context = ContextModel()

    current = state_a
    count = 0
    while True:
        if count == 10:
            break
        current = current.next(context)
        count += 1


if __name__ == "__main__":
    entry()
