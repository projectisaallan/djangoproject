from django.urls import path
from . import views

urlpatterns = [
    path('base', views.welcomed, name='welcomed'),
    path('video', views.upload_video, name='upload_video'),
    path('note', views.upload_note, name='upload_note'),
    path('audio', views.upload_audio, name='upload_audio'),
    path('videos/', views.video_list, name='video_list'),
    path('notes/', views.note_list, name='note_list'),
    path('audios/', views.audio_list, name='audio_list'),
    path('notes_detail/<str:pk>/',views.detail,name='details'),
    path('media/<int:pk>/', views.serve_media, name='serve_media'),
]