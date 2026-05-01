from django.core.exceptions import ValidationError


def blank_validator(value):
    if not value.strip():
        raise ValidationError("El autor no puede estar vacio")


def min_length_validator(min):
    def validator(value):
        if len(value) < min:
            raise ValidationError(f"El resumen tiene que tener mas de {min} caracteres")

    return validator


def range_validator(min: int, max: int):
    if min > max:
        min, max = max, min

    def validator(value):
        if value < min or value > max:
            raise ValidationError(
                f"La calificacion tiene que estar en un rango entre {min} y {max}"
            )

    return validator
