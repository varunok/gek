# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """
        Creates and saves a User with the given username, email and password.
        """
        if not email:
            raise ValueError('The given email must be set')
        # if not group:
        #     raise ValueError('The given group must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        extra_fields.setdefault('group', User.Group.AD)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('group', User.Group.SA)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


class User(AbstractUser):
    class Group:
        SA = 1
        AD = 2
        CHOICES = (
            (SA, _('Супер администратор')),
            (AD, _('Администратор'))
        )

    username = models.CharField(
        max_length=150,
        blank=True,
        null=True
    )
    email = models.EmailField(
        verbose_name=_('Электронная почта'),
        max_length=255,
        unique=True,
        db_index=True
    )
    avatar = models.ImageField(
        verbose_name=_('Аватар'),
        blank=True,
        upload_to="user/avatar"
    )
    first_name = models.CharField(
        verbose_name=_('Имя'),
        max_length=40,
        blank=True
    )
    last_name = models.CharField(
        verbose_name=_('Фамилия'),
        max_length=40,
        blank=True
    )
    middle_name = models.CharField(
        verbose_name=_('Отчество'),
        max_length=40,
        blank=True
    )
    about_self = models.TextField(
        verbose_name=_('О сотруднике'),
        blank=True,
        null=True
    )
    address = models.CharField(
        verbose_name=_('Адрес'),
        max_length=250,
        null=True,
        blank=True
    )
    phone = models.CharField(
        verbose_name=_('Телефон'),
        max_length=250,
        null=True,
        blank=True
    )
    skype = models.CharField(
        verbose_name='Skype',
        max_length=250,
        null=True,
        blank=True
    )
    specialization = models.CharField(
        verbose_name=_('Специализация'),
        max_length=250,
        null=True,
        blank=True
    )
    extra = models.CharField(
        verbose_name=_('Дополнительно'),
        max_length=250,
        null=True,
        blank=True
    )
    video = models.TextField(
        verbose_name=_('Код видео'),
        blank=True,
        null=True
    )
    group = models.IntegerField(
        verbose_name=_('Група'),
        choices=Group.CHOICES
    )

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['group']

    class Meta:
        verbose_name = _('Пользователь')
        verbose_name_plural = _('Пользователи')

    def __unicode__(self):
        return self.email

    def get_full_name(self):
        full_name = '%s %s %s' % (self.first_name, self.last_name, self.middle_name)
        return full_name.strip()

    def get_absolute_url(self):
        return reverse('users:profile', args=[self.id])

    def save(self, *args, **kwargs):
        # if self.is_superuser:
        #     self.group = self.Group.SA
        if self.group == 1:
            self.is_superuser = True
        elif self.group == 2:
            self.is_superuser = False

        super(User, self).save(*args, **kwargs)
