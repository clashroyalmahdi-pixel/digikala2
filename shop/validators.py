from django.core.exceptions import ValidationError

class CustomMinimumLengthValidator:
    def __init__(self, min_length=8):
        self.min_length = min_length

    def validate(self, password, user=None):
        if len(password) < self.min_length:
            raise ValidationError(
                f'رمز عبور باید حداقل {self.min_length} کاراکتر باشد.',
                code='password_too_short',
            )

    def get_help_text(self):
        return f'رمز عبور باید حداقل {self.min_length} کاراکتر باشد.'
