from validator.schemas.string_schema import StringSchema

class Validator:

    def __init__(self):
        self.schema = None

    def string(self) -> StringSchema:
        self.schema = StringSchema()
        return self.schema
