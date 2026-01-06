# test/conftest.py
import pytest 

# This is a "Fixture". It provides data to any test that asks for it.
@pytest.fixture
def sample_data():
    return [100, 200, 50]