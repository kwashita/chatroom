from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import related

# Create your models here.


class Userinfo(models.Model):
    nickName = models.CharField(null=True, blank=True, max_length=100)
    photo = models.ImageField(null=True, blank=True,
                              upload_to="profile_photo/")
    belong = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="userinfo_user", null=True, blank=True)

    def __int__(self):
        return self.id
