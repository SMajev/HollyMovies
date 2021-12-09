from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    biography = models.TextField()

    def delete(self, using=None, keep_parents=False):
        self.user.delete()
        return super().delete(using, keep_parents)



