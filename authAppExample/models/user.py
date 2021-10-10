from django.db                   import models
from django.contrib.auth.models  import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.contrib.auth.hashers import make_password
 

class UserManager(BaseUserManager):
    def create_user(self, username, password=None):
        """
        Creates and saves a user with the given username and password.
        """
        if not username:
            raise ValueError('Debes tener un usuario')
        user = self.model(username=username)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password):
        """
        Creates and saves a superuser with the given username and password.
        """
        user = self.create_user(
            username=username,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    id          = models.BigAutoField(primary_key=True)
    username    = models.CharField('Nombre', max_length = 25, unique=True)
    apellido    = models.CharField("Apellido", max_length = 25, unique = True, default="")
    cedula      = models.CharField("Cedula", max_length=15, unique=True,default = 0)
    password    = models.CharField('Password', max_length = 256)
    email       = models.EmailField('Email',   max_length = 100)
    
     
    def save(self, **kwargs):
        some_salt = 'mMUj0DrIK6vgtdIYepkIxN'
        self.password = make_password(self.password, some_salt)
        super().save(**kwargs)
    
    objects = UserManager()
    USERNAME_FIELD = 'username'
