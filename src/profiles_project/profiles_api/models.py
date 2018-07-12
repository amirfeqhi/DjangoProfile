from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager, PermissionsMixin)
from django.db import models


class UserProfileManager(BaseUserManager):
    """Helps django to work with users."""

    def create_user(self, email, name, password=None):
        """Creating user."""

        if not email:
            raise ValueError('An email required.')

        email = self.normalize_email(email)
        user = self.model(email=email, name=name)

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, name, password):
        """Creating superuser."""

        user = self.create_user(email, name, password)

        user.is_superuser = True
        user.is_staff = True

        user.save(using=self._db)

        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """This models is showing our user profiles."""

    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email' 
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        """Used to get a user full name."""

        return self.name

    def get_short_name(self):
        """Used to get a user short name."""

        return self.name

    def __str__(self):
        """Representation of the objects in string form."""

        return self.email


class ProfileFeedItem(models.Model):
    """Profile status update."""

    user_profile = models.ForeignKey('UserProfile', on_delete=models.CASCADE)
    status_text = models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Represent of ProfileFeedItem objects."""

        return self.status_text
