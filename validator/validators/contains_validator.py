from .base_validator import BaseValidator
from typing import Iterable

class ContainsValidator(BaseValidator):
    
    def __init__(self, iterable: Iterable) -> None:
        self.iterable = iterable
    
    def validate(self, value: Iterable) -> bool:
        return self.iterable in value

    def get_validator_name(self) -> str:
        return "contains_validator"