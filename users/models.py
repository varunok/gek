# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, group, **extra_fields):
        """
        Creates and saves a User with the given username, email and password.
        """
        if not email:
            raise ValueError('The given email must be set')
        if not group:
            raise ValueError('The given group must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email=None, password=None, group=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, group, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('group', 1)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


class User(AbstractUser):
    class Group:
        SA = 1
        AD = 2
        MOD = 3
        CHOICES = (
            (SA, 'Супер администратор'),
            (AD, 'Администратор'),
            (MOD, 'Модератор')
        )

    username = models.CharField(
        max_length=150,
        blank=True,
        null=True
    )
    email = models.EmailField(
        verbose_name='Электронная почта',
        max_length=255,
        unique=True,
        db_index=True
    )
    avatar = models.ImageField(
        verbose_name='Аватар',
        blank=True,
        null=True,
        upload_to="user/avatar"
    )
    first_name = models.CharField(
        verbose_name='Имя',
        max_length=40,
        null=True,
        blank=True
    )
    last_name = models.CharField(
        verbose_name='Фамилия',
        max_length=40,
        null=True,
        blank=True
    )
    middle_name = models.CharField(
        verbose_name='Отчество',
        max_length=40,
        null=True,
        blank=True
    )
    about_self = models.TextField(
        verbose_name='О сотруднике',
        blank=True,
        null=True
    )
    address = models.CharField(
        verbose_name='Адрес',
        max_length=250,
        null=True,
        blank=True
    )
    phone = models.CharField(
        verbose_name='Телефон',
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
        verbose_name='Специализация',
        max_length=250,
        null=True,
        blank=True
    )
    extra = models.CharField(
        verbose_name='Дополнительно',
        max_length=250,
        null=True,
        blank=True
    )
    video = models.TextField(
        verbose_name='Код видео',
        blank=True,
        null=True
    )
    group = models.IntegerField(
        verbose_name='Група',
        choices=Group.CHOICES
    )

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __unicode__(self):
        return self.email

    def get_full_name(self):
        full_name = '%s %s %s' % (self.first_name, self.last_name, self.middle_name)
        return full_name.strip()
