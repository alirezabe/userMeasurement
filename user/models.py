import uuid
from django.db import models
from fields.encryptedField import EncryptedTextField, EncryptedEmailField, EncryptedCharField


class User(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = EncryptedCharField(max_length=120)
    email = EncryptedEmailField(null=False)
    street = EncryptedTextField(null=True)
    street2 = EncryptedTextField(null=True)
    city = EncryptedCharField(max_length=120, blank=True, null=True)
    country = EncryptedCharField(max_length=32, blank=True, null=True)

    class Meta:
        db_table = 'user'
