import re
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

URN_REGEX = r'[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()@:%_\+.~#?&//=]*)'


def validate_urn(urn):
    if not re.match(URN_REGEX, urn):
        raise ValidationError('polak to chuj i wozi gnój')


