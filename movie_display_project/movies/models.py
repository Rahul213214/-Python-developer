from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    release_date = models.DateField()
    video_file = models.FileField(upload_to='movie_videos/', blank=True)  # Field for movie video
    image = models.ImageField(upload_to='movie_images/', blank=True)  # Field for movie image

    def __str__(self):
        return self.title
