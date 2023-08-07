from django.db import models

class Video(models.Model):
    title = models.CharField(max_length=200)
    video_file = models.FileField(upload_to='videos/')
    def __str__(self) -> str:
        return self.title

class Note(models.Model):
    title = models.CharField(max_length=200)
    note_file = models.FileField(upload_to='note/',default='')
    content = models.TextField()
    def __str__(self) -> str:
        return self.title

class Audio(models.Model):
    title = models.CharField(max_length=200)
    audio_file = models.FileField(upload_to='audio/')
    def __str__(self) -> str:
        return self.title
    
class MediaFile(models.Model):
    title = models.CharField(max_length=100)
    file = models.FileField(upload_to='media/')
    def __str__(self) -> str:
        return self.title