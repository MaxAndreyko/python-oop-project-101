from abc import ABC, abstractmethod
from typing import Any

class BaseValidator(ABC):

    @abstractmethod
    def validate(self, value: Any) -> bool:
        raise NotImplementedError
    
    @abstractmethod
    def get_validator_name(self) -> str:
        raise NotImplementedError