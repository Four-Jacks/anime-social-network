from django.contrib import admin

from .models import Anime, Season


class AnimeAdmin(admin.ModelAdmin):
    list_display = ("title", "title_jap", "img_url", "type", "season", "status", "air_date", "synopsis")


class SeasonAdmin(admin.ModelAdmin):
    list_display = ("season", "year")


admin.site.register(Anime, AnimeAdmin)
admin.site.register(Season, SeasonAdmin)
