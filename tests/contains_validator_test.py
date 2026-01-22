import pytest
from validator.validators.contains_validator import ContainsValidator

@pytest.fixture
def validator_factory():
    def _create_validator(iterable):
        return ContainsValidator(iterable)
    return _create_validator

class TestContainsValidatorInitialization:
    """Test cases for __init__ method"""

    def test_basic_initialization(self, validator_factory):
        """Test basic initialization"""
        validator = validator_factory("string")
        assert validator.iterable == "string"
    
class TestContainsValidatorValidate:

    @pytest.mark.parametrize("iterable,contain_value,contain_flag", [
        pytest.param("string", "some string", True, id="string_iterable_true"),
        pytest.param("string", "any", False, id="string_iterable_false"),
        pytest.param(1, [1, 2, 3], True, id="list_iterable_true"),
        pytest.param(1, [2, 3], False, id="list_iterable_false"),
        pytest.param(1, {1, 2, 3},True, id="set_iterable_true"),
        pytest.param(1, {2, 3}, False, id="set_iterable_false"),
    ])
    def test_validate_with_various_iterables(self, iterable, contain_value, contain_flag, validator_factory):
        validator = validator_factory(iterable)
        assert validator.validate(contain_value) is contain_flag

class TestContainsValidatorGetValidatorName:
    def test_get_validator_name(self, validator_factory):
        validator = validator_factory([])
        assert validator.get_validator_name() == "contains_validator"
