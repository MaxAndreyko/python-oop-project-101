from unittest.mock import Mock
import pytest
from validator.validators.len_validator import LenValidator

@pytest.fixture
def validator_factory():
    def _create_validator(len, type=None):
        if not type:
            return LenValidator(len)
        return LenValidator(len, type)
    return _create_validator

@pytest.fixture
def no_len_object():
    return Mock()

class TestLenValidatorInitialization:
    """Test cases for __init__ method"""

    def test_basic_initialization(self, validator_factory):
        """Test basic initialization"""
        validator = validator_factory(3, "max")
        assert validator._len == 3
        assert validator.type == "max"
    
    def test_default_arguments_initialization(self, validator_factory):
        """Test initialization with default arguments"""
        validator = validator_factory(None)
        assert validator._len == 0
        assert validator.type == "min"

class TestLenValidatorValidate:

    @pytest.mark.parametrize("len,type,value,len_flag", [
        pytest.param(20, "max", "some string", True, id="string_within_len"),
        pytest.param(10, "max", "some string", False, id="string_outside_len"),
        pytest.param(5, "max", [1, 2, 3], True, id="list_within_len"),
        pytest.param(1, "max", [1, 2, 3], False, id="list_outside_len"),
        pytest.param(5, "max", {1, 2, 3}, True, id="set_within_range"),
        pytest.param(1, "max", {1, 2, 3}, False, id="set_outisde_range"),
    ])
    def test_validate_max_len_with_various_iterables(self, len, type, value, len_flag, validator_factory):
        validator = validator_factory(len, type)
        assert validator.validate(value) is len_flag

    @pytest.mark.parametrize("len,type,value,len_flag", [
        pytest.param(20, "min", "some string", False, id="string_less_len"),
        pytest.param(10, "min", "some string", True, id="string_greater_len"),
        pytest.param(5, "min", [1, 2, 3], False, id="list_less_len"),
        pytest.param(1, "min", [1, 2, 3], True, id="list_greater_len"),
        pytest.param(5, "min", {1, 2, 3}, False, id="set_less_range"),
        pytest.param(1, "min", {1, 2, 3}, True, id="set_greater_range"),
    ])
    def test_validate_min_len_with_various_iterables(self, len, type, value, len_flag, validator_factory):
        validator = validator_factory(len, type)
        assert validator.validate(value) is len_flag

    @pytest.mark.parametrize("len,type", [
        pytest.param(10, "max", id="no_len_obj_max"),
        pytest.param(1, "min", id="no_len_obj_min"),
    ])
    def test_validate_no_len_object_always_return_false(self, len, type, no_len_object, validator_factory):
        validator = validator_factory(len, type)
        assert validator.validate(no_len_object) is False

        
class TestLenValidatorGetValidatorName:
    def test_get_validator_name(self, validator_factory):
        validator = validator_factory(5)
        assert validator.get_validator_name() == "min_len_validator"