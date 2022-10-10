from django.db import models
from django.contrib.auth.models import UserManager


class PersonQuerySet(models.QuerySet):
    def all_user(self):
        return self.filter(role=0)

    def all_manager(self):
        return self.filter(role=1)

    def all_admin(self):
        return self.filter(role=2)


class OnlyManager(UserManager):
    def get_queryset(self):
        return PersonQuerySet(self.model, using=self._db)

    def all_admin(self):
        return self.get_queryset().all_admin()

    def all_manager(self):
        return self.get_queryset().all_manager()