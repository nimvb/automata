import json

from app.model.core.context import ContextModel, ContextType, StateType
from app.model.core.state import StateModel
from app.model.core.transition import TransitionModel


def entry():
    state_a = StateModel(StateType.Login)
    state_b = StateModel(StateType.Captcha)
    transition_a_b = TransitionModel(state_b)
    transition_b_a = TransitionModel(state_a)
    state_a.transitions.append(transition_a_b)
    state_b.transitions.append(transition_b_a)

    context = ContextModel()
    context.type = ContextType.Start

    current = state_a
    count = 0
    while True:
        if count == 10:
            break
        current = current.next(context)
        count += 1


if __name__ == "__main__":
    entry()
