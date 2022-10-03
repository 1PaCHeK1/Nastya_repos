from django.dispatch import receiver
from django.db.models.signals import (
    pre_save, 
    post_save,
    pre_delete,
    post_delete
)
from django.db.models import Count
from .models import UserManager, User

import logging
logger = logging.getLogger(__name__)



def get_most_free_manager() -> User:
    logger.error("Получили самого свободного пользователя")
    ums = (UserManager.objects
          .values('manager')
          .annotate(amount_user=Count('manager'))
    )
    um = max(ums, key=lambda item: item['amount_user'])
    return User.manager_objects.get(id=um['manager'])


@receiver(post_save, sender=User)
def create_relation_userManager(sender, instance:User, *args, **kwargs):
    if kwargs.get('created', False):
        manager = get_most_free_manager()
        UserManager.objects.create(user=instance,
                                   manager=manager)