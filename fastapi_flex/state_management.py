from fastapi import Depends

class StateManager:
    def __init__(self):
        self.state = {}

    def get_state(self, key: str):
        return self.state.get(key, None)

    def set_state(self, key: str, value):
        self.state[key] = value

def get_state_manager():
    return StateManager()
