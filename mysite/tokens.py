import six
import hashlib
import datetime

from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils import baseconv

class CustomTokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, user, timestamp):
        return (
            six.text_type(user.pk) + six.text_type(timestamp) +
            six.text_type(hashlib.sha256(six.text_type(user.pk).encode('utf-8') +
            six.text_type(timestamp).encode('utf-8') +
            six.text_type(user.email).encode('utf-8')).hexdigest())
        )

custom_token_generator = CustomTokenGenerator()