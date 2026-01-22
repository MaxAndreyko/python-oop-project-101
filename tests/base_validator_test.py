import pytest
from validator.validators import BaseValidator
from typing import Any

class DummyValidator(BaseValidator):
    """Dummy validator implementation"""

    def validate(self, value: Any) -> bool:
        return super().validate(value)
    
    def get_validator_name(self) -> str:
        return super().get_validator_name()

class TestBaseValidatorAbstractMethods:
    def test_base_validator_init_raises_type_error(self):
        with pytest.raises(TypeError):
            _ = BaseValidator()

    def test_base_validator_methods_call_raises_not_implemented_error(self):
        dummy_validator = DummyValidator()
        with pytest.raises(NotImplementedError):
            dummy_validator.validate(None)
        with pytest.raises(NotImplementedError):
            dummy_validator.get_validator_name()