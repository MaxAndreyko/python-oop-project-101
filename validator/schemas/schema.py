from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Dict, Any, Optional
from validator.validators import BaseValidator

class Schema(ABC):
    def __init__(self,
                 validators: Optional[Dict[str, BaseValidator]] = None,
                 required: Optional[bool] = False) -> None:
        self.validators = validators or {}
        self._required = required

    def add_validator(self, validator: BaseValidator) -> None:
        self.validators[validator.get_validator_name()] = validator

    @abstractmethod
    def required(self) -> Schema:
        raise NotImplementedError

    def is_valid(self, value: Any) -> bool:
        return all(validator.validate(value) for validator in self.validators.values())

    def _create_instance(self) -> Schema:
        return self.__class__(self.validators, self._required)

