import pytest
from validator.validators.required_validator import RequiredValidator

@pytest.fixture
def validator_factory():
    def _create_validator(null_values):
        return RequiredValidator(null_values)
    return _create_validator

@pytest.fixture
def sample_null_values():
    return ["", None, "null"]

class TestRequiredValidatorInitialization:
    """Test cases for __init__ method"""

    def test_basic_initialization(self, validator_factory, sample_null_values):
        """Test basic initialization"""
        validator = validator_factory(sample_null_values)
        assert validator.null_values == sample_null_values

    def test_default_arguments_initialization(self, validator_factory):
        """Test initialization with default arguments"""
        validator = validator_factory(None)
        assert validator.null_values == []

class TestRequiredValidatorValidate:

    @pytest.mark.parametrize("null_values,value,req_flag", [
        pytest.param(["", "null"], "some string", True, id="not_null_string"),
        pytest.param(["", "null"], "null", False, id="null_string"),
        pytest.param([None, 0], 1, True, id="not_null_int"),
        pytest.param([None, 0], 0, False, id="null_int"),
        pytest.param(None, None, True, id="no_null_values_configured"),
    ])
    def test_validate_required_with_various_null_values(self, null_values, value, req_flag, validator_factory):
        validator = validator_factory(null_values)
        assert validator.validate(value) is req_flag

class TestRequiredValidatorGetValidatorName:
    def test_get_validator_name(self, validator_factory):
        validator = validator_factory(None)
        assert validator.get_validator_name() == "required_validator"