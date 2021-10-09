from django.db import models
from user.models import User


class Measurement(models.Model):
    user_id = models.UUIDField(null=False, blank=False)
    weight = models.PositiveSmallIntegerField(null=True)
    height = models.PositiveSmallIntegerField(null=True)
    width = models.PositiveSmallIntegerField(null=True)
    datetime = models.DateTimeField(auto_created=True, auto_now_add=True)

    def save(self, *args, **kwargs):
        try:
            User.objects.using('user_db').get(id=self.user_id)
            super(Measurement, self).save(*args, **kwargs)
        except User.DoesNotExist:
            raise User.DoesNotExist
        except Exception as e:
            raise e

    class Meta:
        db_table = 'measurement'

