from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from anime.models import Anime


# Creates a user profile object for user preferences
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=100, default='')
    favorite_anime = models.CharField(max_length=100, default='')

    def __str__(self):
        return self.user.username

    def create_profile(sender, **kwargs):
        if kwargs['created']:
            user_profile = UserProfile.objects.create(user=kwargs['instance'])

    post_save.connect(create_profile, sender=User)


# Creates anime to user relationships
class UserAnime(models.Model):
    objects = models.Manager()
    anime = models.ManyToManyField(Anime)
    current_anime = models.ForeignKey(User, related_name='owner', null=True, on_delete=models.PROTECT)

    @classmethod
    def add_anime(cls, current_anime, added_anime):
        anime, added = cls.objects.get_or_create(
            current_anime=current_anime
        )
        anime.users.add(added_anime)

    @classmethod
    def remove_anime(cls, current_anime, added_anime):
        anime, added = cls.objects.get_or_create(
            current_anime=current_anime
        )
        anime.users.remove(added_anime)


# Creates user to user relationships(aka friends)
class UserFriend(models.Model):
    objects = models.Manager()
    friend = models.ManyToManyField(User)
    current_user = models.ForeignKey(User, related_name='has_friend', null=True, on_delete=models.PROTECT)

    @classmethod
    def remove_friend(cls, current_user, new_friend):
        friend, created = cls.objects.get_or_create(
            current_user=current_user
        )
        friend.users.add(new_friend)

    @classmethod
    def lose_friend(cls, current_user, new_friend):
        friend, created = cls.objects.get_or_create(
            current_user=current_user
        )
        friend.users.remove(new_friend)

