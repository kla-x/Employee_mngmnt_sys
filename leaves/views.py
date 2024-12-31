from django.shortcuts import render, redirect


from django.contrib.auth.decorators import login_required
from .models import LeaveRequest
from .forms import LeaveRequestForm

@login_required
def leave_view(request):
    if request.method == 'POST':
        form = LeaveRequestForm(request.POST)
        if form.is_valid():
            leave_request = form.save(commit=False)
            leave_request.user = request.user
            leave_request.save()
            return redirect('leave')
    else:
        form = LeaveRequestForm()

    leave_requests = LeaveRequest.objects.filter(user=request.user)
    return render(request, 'leaves/leave.html', {'form': form, 'leave_requests': leave_requests})
