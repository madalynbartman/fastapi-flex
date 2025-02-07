import pytest
from fastapi_flex.state_management import StateManager

@pytest.fixture
def state_manager():
    return StateManager()

def test_set_get_state(state_manager):
    state_manager.set_state("key1", "value1")
    assert state_manager.get_state("key1") == "value1"

def test_get_nonexistent_state(state_manager):
    assert state_manager.get_state("nonexistent_key") is None
