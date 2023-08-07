

# Create your views here.
from django.shortcuts import render, get_object_or_404,redirect
from django.contrib.auth.models import User
from .models import Message

def user_list(request):
    users = User.objects.all()
    return render(request, 'sms1/user_list.html', {'users': users})

def conversation(request, user_id):
    user = get_object_or_404(User, id=user_id)
    messages = Message.objects.filter(sender=request.user, receiver=user) | Message.objects.filter(sender=user, receiver=request.user)
    messages = messages.order_by('timestamp')
    return render(request, 'sms1/conversation.html', {'user': user, 'messages': messages})

def send_message(request, user_id):
    if request.method == 'POST':
        user = get_object_or_404(User, id=user_id)
        content = request.POST.get('content', '')
        message = Message(sender=request.user, receiver=user, content=content)
        message.save()
    return redirect('conversation', user_id=user_id)