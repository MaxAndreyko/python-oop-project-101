from typing import Any, Optional, Literal
from validator.validators.base_validator import BaseValidator


class LenValidator(BaseValidator):
    def __init__(self, len: Optional[int] = None, type: Literal["max", "min"] = "min") -> None:
        self._len = len or 0
        self.type = type
    
    def validate(self, value: Any) -> bool:
        if not hasattr(value, "__len__"):
            return False
        if self.type == "min":
            return len(value) > self._len
        else:
            return len(value) <= self._len
    
    def get_validator_name(self) -> str:
        return self.type + "_len_validator"