from django.db import models
from django.contrib.auth.models import User

from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Profile(models.Model):
    ppic=models.ImageField(upload_to ='ppic') 
    bio=models.TextField(max_length=600, default="Bio")
    phone=models.CharField(max_length=20, default="Phone")
    fname=models.CharField(max_length=30, default="First name")
    lname=models.CharField(max_length=30, default="last name")
    twitter=models.CharField(max_length=100, default="Twitter url")
    facebook=models.CharField(max_length=100, default="facebook url")
    linkedin=models.CharField(max_length=100, default="linkedin url")
    user=models.OneToOneField(User, on_delete=models.CASCADE,primary_key=True)

    def __str__(self):
        return f'{self.user.username} insta-profile'

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()


    def delete_profile(self):
        self.delete()
    
    @classmethod
    def filter_profile_by_id(cls, id):
        profile = Profile.objects.filter(user__id = id).first()
        return profile

    @classmethod
    def search_profile(cls, name):
        return cls.objects.filter(user__username__icontains=name).all()

