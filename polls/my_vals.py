from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

def validate_question(value):
    if not (value.lower().startswith('w') and value.lower().endswith('?')):
        raise ValidationError(
            _('%(value)s is not a question start with W and endswith ?'),
            params={'value': value},
        )


def validate_choice(value):
    if ' ' in value:
        raise ValidationError(
            _('%(value)s has spaces :(('),
            params={'value': value},
        )