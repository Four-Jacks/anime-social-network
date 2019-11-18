from anime.models import Anime
from jikanpy import Jikan, exceptions

jikan = Jikan()

idx = 1
for _ in range(1, 41000):
    try:
        json = jikan.anime(idx)
        Anime.objects.create(title=json['title'], title_jap=json['title_japanese'], img_url=json['image_url'], type=json['type'], season=json['premiered'], status=json['status'], air_date=json['aired']['string'], synopsis=json['synopsis'])
    except exceptions.APIException as e:
        pass
    idx += 1
