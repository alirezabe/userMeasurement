import uuid
from django.test import TestCase

from user.models import User
from measurement.models import Measurement


class UserTestClass(TestCase):
    databases = '__all__'
    user_id = uuid.uuid4()

    @classmethod
    def setUpTestData(cls):
        User.objects.create(id=cls.user_id, name='Alireza', email='hi@beydaghi.com')

    def test_create(self):
        Measurement.objects.create(user_id=self.user_id, weight=120, height=200)
        self.assertTrue(True)

    def test_invalid_user_id(self):
        try:
            Measurement.objects.create(id=uuid.uuid4(), weight=120, height=200)
        except User.DoesNotExist:
            self.assertFalse(False)
            return
        self.assertTrue(False)
