from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import CommunityMessage, DepartmentMessage, Notification
from accounts.models import User

@login_required
def community_chat(request):
    messages = CommunityMessage.objects.order_by('timestamp')
    users = User.objects.all()
    if request.method == 'POST':
        content = request.POST.get('content')
        message = CommunityMessage(sender=request.user, content=content)
        message.save()
        return redirect('community_chat')
    return render(request, 'chats/community_chat.html', {'messages': messages, 'users': users})

@login_required
def department_chat(request):
    department = request.user.department
    messages = DepartmentMessage.objects.filter(sender__department=department).order_by('timestamp')
    users = User.objects.filter(department=department)
    if request.method == 'POST':
        content = request.POST.get('content')
        message = DepartmentMessage(sender=request.user, content=content)
        message.save()
        return redirect('department_chat')
    return render(request, 'chats/department_chat.html', {'messages': messages, 'users': users})

@login_required
def notifications_board(request):
    if request.user.is_dep_lead or request.user.is_superuser:
        if request.method == 'POST':
            content = request.POST.get('content')
            notification = Notification(sender=request.user, content=content)
            notification.save()
            return redirect('notifications_board')
    notifications = Notification.objects.order_by('timestamp')
    return render(request, 'chats/notifications_board.html', {'notifications': notifications})