from .models import User, UserProfie
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
@receiver(post_save, sender=User)

def post_save_create_profile_recever(sender, instance , created,**kwargs):
    
    if created:
        print('created user profile')
        UserProfie.objects.create(user=instance)
    else:
        try:
            userprofile =  UserProfie.objects.get(user=instance)
            userprofile.save()
            print('user is updated profile')
        except:
            print('profile doesnnot exit to need to create one')
            UserProfie.objects.create(user=instance)



# post_save.connect(post_save_create_profile_recever, sender=User)
@receiver(post_save,sender=User)
def pre_save_profile_reverse(sender, instance,**kwargs):
    # UserProfie.objects.create(user=instance)
    print(instance.username,'the profile is been saved successfully')