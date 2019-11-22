from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin

from django.utils.translation import ugettext_lazy as _
from django.core.mail import send_mail

# Create your models here.

class MyUserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError("L'adresse email doit être renseignée")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', False)
        extra_fields.setdefault('is_staff', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')

        return self._create_user(email, password, **extra_fields)

class MyUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('E-mail'), unique=True, )
    last_name = models.CharField(_('nom'), max_length=30)
    first_name = models.CharField(_('prénom'), max_length=30)
    date_joined = models.DateTimeField(_("date d'enregistrement"), auto_now_add=True)
    is_active = models.BooleanField(_('profile actif'), default=True)
    is_staff = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _('client')
        verbose_name_plural = _('clients')

    def get_full_name(self):
        '''
        Returns the first_name plus the last_name, with a space in between.
        '''
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        '''
        Returns the short name for the user.
        '''
        return self.first_name

    def email_user(self, subject, message, from_email=None, **kwargs):
        '''
        Sends an email to this User.
        '''
        send_mail(subject, message, from_email, [self.email], **kwargs)

class ProfileCustomer(models.Model):
    user = models.OneToOneField(MyUser, on_delete=models.CASCADE, related_name='profile_customer')
    birth_date = models.DateField(_("date d'anniversaire"), null=True, blank=True)
    newsletter = models.BooleanField(default=False)
    adresse_defaut = models.ForeignKey('Address', null=True, on_delete=models.SET_NULL, related_name="selected_address")

class Address(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name="addresses", related_query_name="address")
    nom = models.CharField(_('Nom'), max_length=30)
    prenom = models.CharField(_('prénom'), max_length=30)
    societe = models.CharField(_("nom de l'entreprise"), max_length=30, null=True, blank=True)
    phone = models.PositiveIntegerField(_('téléphone'))
    numetvoie = models.CharField(_('numéro et nom de la rue'), max_length=50)
    post_code = models.PositiveIntegerField(_('code postal'))
    city = models.CharField(_('ville'), max_length=30)
    other_info = models.CharField(_('informations complémentaires'), max_length=50, null=True, blank=True)

    def __str__(self):
        return '%s %s' % (self.user, self.id)

    class Meta:
        ordering = ['user', 'id']