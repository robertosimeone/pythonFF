from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.contrib.auth.hashers import make_password


def get_profile_image_filepath(self):
    return f'profile_images/{self.pk}/{"profile_image.png"}'


def get_default_profile_image():
    return "default/logo_1080_1080.png"


class MyAccountManager(BaseUserManager):
    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError("Users must have an email")
        if not username:
            raise ValueError("Users must have an username")
        if not password:
            raise ValueError("Users must have a password")
        user = self.model(email=self.normalize_email(email), username=username, )
        user.password = make_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password):
        user = self.create_user(email=self.normalize_email(email), username=username,
                                password=password)
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class Movie(models.Model):
    name = models.CharField(verbose_name="title", max_length=90)
    duration = models.IntegerField(verbose_name="movie duration", default=0)
    description = models.TextField(verbose_name="movie description", default='')
    price = models.DecimalField(verbose_name="movie price", decimal_places=2, max_digits=5, default=0)
    image = models.ImageField(verbose_name="movie image", max_length=255, upload_to=None, null=True, blank=True,
                              default=None)

    def __str__(self):
        return self.name


# Create your models here.
class User(AbstractBaseUser):
    username = models.CharField(max_length=30)
    email = models.EmailField(verbose_name="email", max_length=70, unique=True)
    token = models.DecimalField(verbose_name="token balance", decimal_places=2, max_digits=100000, default=0)
    streak_number = models.IntegerField(verbose_name="streak number", default=0)
    date_joined = models.DateTimeField(verbose_name="date joined", auto_now_add=True)
    last_login = models.DateTimeField(verbose_name="last login", auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    # get_profile_image_filepath
    # get_default_profile_image
    profile_image = models.ImageField(max_length=255, upload_to=None, null=True, blank=True,
                                      default=None)
    subscribed_movies = models.ManyToManyField(Movie, blank=True)

    objects = MyAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def str(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True


# def get_profile_image_filename(self):
# return str(self.profile_image)[str(self.profile_image).index(f'profile_images/{self.pk}/'):]


class Statistic(models.Model):
    movies_watched = models.IntegerField(default=0)
    movies_liked = models.IntegerField(default=0)
    comment_counter = models.IntegerField(default=0)
    likes_counter = models.IntegerField(default=0)

    user = models.ForeignKey(User, related_name="user", on_delete=models.CASCADE)
