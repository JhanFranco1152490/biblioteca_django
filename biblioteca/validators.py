from django.core.exceptions import ValidationError


def blank_validator(value):
    if not value.strip():
        raise ValidationError("El autor no puede estar vacio")


class min_length_validator:
    def __init__(self, min_value: int):
        self.min_value = min_value

    def __call__(self, value: str):
        if len(value) < self.min_value:
            raise ValidationError(
                f"El resumen tiene que tener mas de {self.min_value} caracteres"
            )


class range_validator:
    def __init__(self, min_value: int, max_value: int):
        self.min_value = min_value
        self.max_value = max_value

    def __call__(self, value: int):
        if not self.min_value <= value <= self.max_value:
            raise ValidationError(
                f"La calificacion tiene que estar en un rango entre {self.min_value} y {self.max_value}"
            )
