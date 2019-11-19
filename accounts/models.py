from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from anime.models import Anime


# Creates a user profile object for user preferences
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=256, default='I love anime')
    avatar = models.CharField(max_length=256, default='https://thehaletelescope.com/wp-content/uploads/2018/10/weeb.jpg')
    favorite_anime = models.CharField(max_length=256, default='Cowboy Bebop')

    def __str__(self):
        return self.user.username

    def create_profile(sender, **kwargs):
        if kwargs['created']:
            user_profile = UserProfile.objects.create(user=kwargs['instance'])

    post_save.connect(create_profile, sender=User)

    def edit_profile(sender,**kwargs):
        user_profile = UserProfile.objects.create(user=kwargs['instance'])


# Creates anime to user relationships
class UserAnime(models.Model):
    objects = models.Manager()
    anime = models.ManyToManyField(Anime)
    current_anime = models.ForeignKey(User, related_name='owner', null=True, on_delete=models.PROTECT)

    @classmethod
    def add_anime(cls, current_anime, added_animepk):
        current_anime = User.objects.get(pk=current_anime)
        #added_anime = User.objects.get(pk=current_anime)
        user, added = cls.objects.get_or_create(
            current_anime=current_anime
        )
        try:
            user.anime.add(added_animepk)
        except:
            pass

    @classmethod
    def remove_anime(cls, current_anime, added_animepk):
        added_anime = User.objects.get(pk=current_anime)
        user, added = cls.objects.get_or_create(
            current_anime=current_anime
        )
        user.anime.remove(added_animepk)

# Creates user to user relationships(aka friends)
class UserFriend(models.Model):
    objects = models.Manager()
    friend = models.ManyToManyField(User)
    current_user = models.ForeignKey(User, related_name='has_friend', null=True, on_delete=models.PROTECT)

    @classmethod
    def add_friend(cls, current_userpk, new_friendpk):
        current = User.objects.get(pk=current_userpk)
        current_user = User.objects.get(pk=new_friendpk)
        if current != current_user:
            current_user, created = cls.objects.get_or_create(
                current_user=current_user
            )
            try:
                current_user.friend.add(current_userpk)
            except:
                pass

            current_user = current
            current_user, created = cls.objects.get_or_create(
                current_user=current_user
            )
            try:
                current_user.friend.add(new_friendpk)
            except:
                pass

    @classmethod
    def remove_friend(cls, current_userpk, new_friendpk):
        current = User.objects.get(pk=current_userpk)
        current_user = User.objects.get(pk=new_friendpk)
        if current != current_user:
            current_user, created = cls.objects.get_or_create(
                current_user=current_user
            )
            current_user.friend.remove(current_userpk)
            current_user = current
            current_user, created = cls.objects.get_or_create(
                current_user=current_user
            )
            current_user.friend.remove(new_friendpk)
