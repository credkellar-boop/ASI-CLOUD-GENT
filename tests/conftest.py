import pytest
from unittest.mock import MagicMock

class MockStorageProxy:
    def __init__(self):
        self.store = {}
    def get(self, key): return self.store.get(key, None)
    def set(self, key, value): self.store[key] = value

@pytest.fixture
def mock_agent_context():
    """Generates an isolated mock agent context containing memory vectors for testing."""
    context = MagicMock()
    context.storage = MockStorageProxy()
    context.logger = MagicMock()
    return context
