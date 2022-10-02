from django.dispatch import receiver
from django.db.models.signals import (
    pre_save, 
    post_save,
    pre_delete,
    post_delete
)

from .models import UserManager, User



def get_most_free_manager() -> User:
    user_manager = list(UserManager.objects.all().values_list())
    managers_with_user = {}
    for i in user_manager:
        if i[2] not in managers_with_user:
            managers_with_user[i[2]] = 0
        managers_with_user[i[2]] += 1
    all_managers = list(User.manager_objects.all_manager().values_list())
    manager_id = None
    for i in all_managers:
        if i[0] not in managers_with_user:
            return User.manager_objects.all_manager().get(id=i[0])
    manager_id = sorted(managers_with_user.items(), key=lambda item: item[1])[0][0]
    return User.manager_objects.all_manager().get(id=manager_id)


@receiver(post_save, sender=User)
def create_relation_userManager(sender, instance:User, *args, **kwargs):
    if kwargs.get('created', False):
        manager = get_most_free_manager()
        UserManager.objects.create(user=instance,
                                   manager=manager)