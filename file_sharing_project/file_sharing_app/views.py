from django.shortcuts import render, redirect, get_object_or_404
from .forms import VideoForm, NoteForm, AudioForm
from  .models import  Video, Note, Audio, MediaFile
from django.http import FileResponse
from django.contrib.auth.decorators import login_required

@login_required
def upload_video(request):
    if request.method == 'POST':
        form = VideoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('video_list')
    else:
        form = VideoForm()
    return render(request, 'file_sharing_app/upload_video.html', {'form': form})


@login_required
def upload_note(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('note_list')
    else:
        form = NoteForm()
    return render(request, 'file_sharing_app/upload_note.html', {'form': form})

@login_required
def upload_audio(request):
    if request.method == 'POST':
        form = AudioForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('audio_list')
    else:
        form = AudioForm()
    return render(request, 'file_sharing_app/upload_audio.html', {'form': form})

@login_required
def video_list(request):
    videos = Video.objects.all()
    return render(request, 'file_sharing_app/video_list.html', {'videos': videos})

@login_required
def note_list(request):
    notes = Note.objects.all()
    return render(request, 'file_sharing_app/note_list.html', {'notes': notes})

@login_required
def audio_list(request):
    audio_files = Audio.objects.all()
    return render(request, 'file_sharing_app/audio_list.html',{'audio_files': audio_files})

@login_required
def welcomed(request):
    audio_files = Audio.objects.all()
    notes = Note.objects.all()
    videos = Video.objects.all()
    return render(request,'file_sharing_app/index.html',{'audio_files': audio_files, 'notes': notes,'videos': videos})

@login_required
def detail(request):
    contents = Note.objects.all()
    return render(request, 'file_sharing_app/note_detail.html',{
        'contents':contents
    })
@login_required
def serve_media(request, pk):
    media_file = get_object_or_404(MediaFile, pk=pk)
    return  FileResponse(media_file.file, content_type='application/octet-stream')

@login_required
def details(request):
    content = Audio.objects.all()
    return  FileResponse(content.file, content_type='application/octet-stream')
    

@login_required
def log_out(request):
   return render(request, 'login_app/login.html')