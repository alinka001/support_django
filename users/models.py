from django.db import models
from django.contrib.auth.models import User, AbstractUser


class User(AbstractUser):
    ROLE_CHOICES = (
        ('user', 'User'),
        ('worker', 'Worker'),
       # ('admin', 'Admin')
    )

    role = models.CharField(max_length=50, choices=ROLE_CHOICES, default='user')
    # username = models.CharField(max_length=50, unique=False)
    # first_name = models.CharField(max_length=50)
    # last_name = models.CharField(max_length=50)
    # email = models.EmailField(max_length=255, unique=True)
    # password = models.CharField(max_length=150)
    #
    # USERNAME_FIELD = 'email'  # уникальный идентификатор модели
    # REQUIRED_FIELDS = ['username']  # список имен полей которые будут
    #                                 # запрашиваться при создании пользователя
    #                                 # с помощью createsuperuser
    #
    # objects = UserManager()
    #
    # def __str__(self):
    #     return self.email

    # def has_perm(self, perm, obj=None):
    #     return True
    #
    # def has_module_perms(self, app_label):  # шо тут происходит
    #     return True

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, blank=True, null=True)
    email = models.EmailField(max_length=100, blank=True, null=True, unique=True)
    username = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return str(self.username)
