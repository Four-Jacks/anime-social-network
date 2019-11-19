from django.contrib import admin

from .models import Anime


class AnimeAdmin(admin.ModelAdmin):
    list_display = ("title", "title_jap", "img_url", "type", "season", "status", "air_date", "synopsis")


admin.site.register(Anime, AnimeAdmin)
