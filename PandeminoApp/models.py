from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class BlogPost(models.Model):
    title = models.CharField(max_length=50, null=False, blank=False)
    body = models.TextField(max_length=5000, null=False, blank=False)
    slug = models.SlugField(blank = True, unique = True)

    def __str__(self):
        return self.title


# class MyAccountManager(BaseUserManager):
#     def create_user(self, mail, username, password = None):
#         if not mail:
#             raise ValueError("User must have an email address")
#         if not username:
#             raise ValueError("User must have an username")
#
#         user = self.model(
#             mail = self.normalize_email(mail),
#             username = username,
#         )
#
#         user.set_password(password)
#         user.save(using=self._db)
#         return user


class Account(AbstractBaseUser):
    username = models.CharField(max_length = 50, null=False, blank=False, unique = True)
    password = models.CharField(max_length = 200, null = False, blank=False)
    mail = models.CharField(max_length = 50, null = False, blank=False, unique = True)

    # USERNAME_FIELD = 'mail'
    # REQUIRED_FIELDS = ['username','mail','password']
    # objects = MyAccountManager()

    def __str__(self):
        return self.username
