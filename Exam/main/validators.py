from django.core.exceptions import ValidationError
import string
def character_validator(value):
    for char in value:
        if char not in string.digits and char not in string.ascii_letters and char != "_":
            raise ValidationError("Ensure this value contains only letters, numbers, and underscore.")
