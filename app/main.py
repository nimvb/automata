import json

from app.model.core.context import ContextModel, TransitionType, StateType
from app.model.core.state import StateModel
from app.model.core.transition import TransitionModel


def entry():
    state_a = StateModel(StateType.Login)
    state_b = StateModel(StateType.Captcha)
    state_c = StateModel(StateType.Scrap)
    transition_a_b = TransitionModel(state_b, TransitionType.LoginSuccess)
    transition_b_a = TransitionModel(state_a, TransitionType.CaptchaFailure)
    transition_b_c = TransitionModel(state_c,TransitionType.CaptchaSuccess)
    state_a.transitions.append(transition_a_b)
    state_b.transitions.append(transition_b_a)
    state_b.transitions.append(transition_b_c)

    context = ContextModel()
    context.type = TransitionType.Start

    current = state_a
    count = 0
    while True:
        if count == 10:
            break
        current = current.next(context)
        count += 1


if __name__ == "__main__":
    entry()
