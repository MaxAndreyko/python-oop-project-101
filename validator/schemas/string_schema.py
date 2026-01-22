from __future__ import annotations
from typing import Optional, Dict
from validator.validators.base_validator import BaseValidator
from validator.schemas import Schema
from validator.validators.contains_validator import ContainsValidator
from validator.validators.required_validator import RequiredValidator
from validator.validators.len_validator import LenValidator

class StringSchema(Schema):
    def __init__(self,
                 validators: Optional[Dict[str, BaseValidator]] = None,
                 required: Optional[bool] = False) -> None:
        super().__init__(validators, required)

    def contains(self, text: str) -> StringSchema:
        self.add_validator(ContainsValidator(text))
        return self._create_instance()
    
    def required(self) -> StringSchema:
        self._required = True
        self.add_validator(RequiredValidator([None, ""]))
        return self._create_instance()

    def min_len(self, len: int) -> StringSchema:
        self.add_validator(LenValidator(len))
        return self._create_instance()
