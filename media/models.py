"""
Definition of models.
"""

from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.
class Picture(models.Model):
    artist = models.CharField(max_length = 25)
    title = models.CharField(max_length = 50)
    media = models.CharField(max_length = 1000)

    def get_absolute_url(self):
        return reverse('media:detail', kwargs={'pk':self.pk})

    def __str__(self):
        return self.title + ' - ' + self.artist

class Reaction(models.Model):
    picture = models.ForeignKey(Picture, on_delete=models.CASCADE)
    reaction_poster = models.CharField(max_length = 25)
    reaction_title = models.CharField(max_length = 50)
    reaction_description = models.CharField(max_length = 5000)
    is_liked = models.BooleanField(default=False)

    def __str__(self):
        return self.reaction_poster + ' - ' + self.reaction_title