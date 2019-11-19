from django.db import models

# Create your models here.


class Anime(models.Model):
    objects = models.Manager()
    title = models.CharField(max_length=256)
    title_jap = models.CharField(max_length=256, null=True, blank=True, default='N/A')
    img_url = models.CharField(max_length=256, null=True, blank=True, default='https://i.pinimg.com/originals/11/ea/01/11ea01854b381fa350ca6ed8c77fe13b.png')
    type = models.CharField(max_length=5, null=True, blank=True, default='N/A')
    season = models.CharField(max_length=11, null=True, blank=True, default='N/A')
    status = models.CharField(max_length=16, null=True, blank=True, default='N/A')
    air_date = models.CharField(max_length=32, null=True, blank=True, default='N/A')
    synopsis = models.TextField(null=True, blank=True, default="N/A")

    class Meta:
        verbose_name_plural = 'anime'

    def __str__(self):
        return self.title
