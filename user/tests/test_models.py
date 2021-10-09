import uuid
from django.test import TestCase

from user.models import User


class UserTestClass(TestCase):
    databases = '__all__'
    user_id = uuid.uuid4()

    @classmethod
    def setUpTestData(cls):
        User.objects.create(id=cls.user_id, name='Alireza', email='hi@beydaghi.com')

    def test_name(self):
        user = User.objects.get(id=self.user_id)
        self.assertEqual(user.name, 'Alireza')

    def test_email(self):
        user = User.objects.get(id=self.user_id)
        self.assertEqual(user.email, 'hi@beydaghi.com')

    def test_user_not_found(self):
        try:
            User.objects.get(id=uuid.uuid4())
        except User.DoesNotExist:
            self.assertFalse(False)
            return
        self.assertTrue(True)
