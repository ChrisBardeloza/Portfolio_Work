from django.db import models

# Create your models here.
class hero(models.Model):
    hero_name = models.CharField(max_length=200)
    hero_id = models.IntegerField()

class owhighlight(models.Model):
    is_potg = models.BooleanField(default=False)
    hero_vid = models.CharField(max_length=200)
    vid_url = models.URLField()

