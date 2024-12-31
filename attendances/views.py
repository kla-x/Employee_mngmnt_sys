from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Attendance
from .forms import AttendanceForm
from django.utils import timezone

@login_required
def attendance_view(request):
    today = timezone.now().date()
    attendance_obj, created = Attendance.objects.get_or_create(user=request.user, date=today)

    if request.method == 'POST':
        form = AttendanceForm(request.POST, instance=attendance_obj)
        if form.is_valid():
            attendance_obj = form.save(commit=False)
            attendance_obj.status = True  # Set status to True when marking attendance
            attendance_obj.save()
            return redirect('attendance')
    else:
        form = AttendanceForm(instance=attendance_obj)

    attendances = Attendance.objects.filter(user=request.user).order_by('-date')
    return render(request, 'attendances/attendance.html', {'form': form, 'attendances': attendances})