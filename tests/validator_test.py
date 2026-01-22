import pytest
from validator import Validator
from validator.schemas.string_schema import StringSchema

@pytest.fixture
def validator():
    return Validator()

class TestValidatorInitialization:
    """Test cases for __init__ method"""

    def test_basic_initialization(self, validator):
        """Test basic initialization"""
        assert validator.schema is None
    
class TestValidatorStringMethod:
    """Test cases for string method"""

    def test_string_returns_string_schema(self, validator):
        """Test string returns string schema and sets validator schema"""
        string = validator.string()
        assert isinstance(string, StringSchema)
        assert isinstance(validator.schema, StringSchema)