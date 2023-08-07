from django import forms
from .models import Video, Note, Audio

class VideoForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = ['title', 'video_file']

class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['title','content', 'note_file']

class AudioForm(forms.ModelForm):
    class Meta:
        model = Audio
        fields = ['title', 'audio_file']