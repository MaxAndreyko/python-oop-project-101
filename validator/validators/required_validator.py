from .base_validator import BaseValidator
from typing import Any, Optional, List

class RequiredValidator(BaseValidator):
    def __init__(self, null_values: Optional[List] = None) -> None:
        self.null_values = null_values or []

    def validate(self, value: Any) -> bool:
        return value not in self.null_values

    def get_validator_name(self) -> str:
        return "required_validator"