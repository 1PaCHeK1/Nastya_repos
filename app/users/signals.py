from django.dispatch import receiver
from django.db.models.signals import (
    pre_save, 
    post_save,
    pre_delete,
    post_delete
)

from .models import UserManager, User



def get_most_free_manager() -> User:
    return User.manager_objects.all_manager().first()


@receiver(post_save, sender=User)
def create_relation_userManager(sender, instance:User, *args, **kwargs):
    if kwargs.get('created', False):
        manager = get_most_free_manager()
        UserManager.objects.create(user=instance,
                                   manager=manager)