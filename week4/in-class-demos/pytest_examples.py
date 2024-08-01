import pytest

# test_parametrize.py
# @pytest.mark.parametrize runs the test_addition function with each pair of input and expected values.
# The test checks if adding 1 to input gives the expected result.
@pytest.mark.parametrize("input, expected", [(1, 2), (3, 4), (5, 6)])
def test_addition(input, expected):
    result = input + 1
    assert result == expected
    
# test_fixtures.py
# @pytest.fixture defines a setup function (sample_data) that returns a value.
# test_with_fixture uses this fixture to get the setup data.
@pytest.fixture
def sample_data():
    return "data"

def test_with_fixture(sample_data):
    assert sample_data == "data"

# test_assertions.py
def test_simple_assertions():
    a = 10
    b = 10
    assert a == b 