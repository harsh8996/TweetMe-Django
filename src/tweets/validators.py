from django.core.exceptions import ValidationError

def  validate_content(value):
    if value == '1234':
        raise ValidationError('error.446..')
    return value