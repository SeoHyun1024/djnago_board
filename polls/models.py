from django.db import models

class board (models.Model):
    title = models.CharField(max_length= 200)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    photo = models.ImageField(blank=True,null=True,upload_to = 'board_photo')

    def __str__(self):
        return self.title