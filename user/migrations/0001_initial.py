# Generated by Django 3.2.8 on 2021-10-09 02:13

from django.db import migrations, models
import fields.encryptedField
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', fields.encryptedField.EncryptedCharField(max_length=120)),
                ('email', fields.encryptedField.EncryptedEmailField(max_length=254)),
                ('street', fields.encryptedField.EncryptedTextField(null=True)),
                ('street2', fields.encryptedField.EncryptedTextField(null=True)),
                ('city', fields.encryptedField.EncryptedCharField(blank=True, max_length=120, null=True)),
                ('country', fields.encryptedField.EncryptedCharField(blank=True, max_length=32, null=True)),
            ],
            options={
                'db_table': 'user',
            },
        ),
    ]
