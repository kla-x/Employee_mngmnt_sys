from django.shortcuts import render

from django.contrib.auth.decorators import login_required, user_passes_test
from accounts.models import User, Department
from leaves.models import LeaveRequest
from payrolls.models import Payroll
from attendances.models import Attendance
from django.db.models import Q, Sum

@user_passes_test(lambda u: u.is_superuser or u.role.name == 'Department Head')
@login_required
def reports_view(request):
    departments = Department.objects.all()
    leave_requests = LeaveRequest.objects.all()
    payrolls = Payroll.objects.all()
    attendances = Attendance.objects.all()

    

    if request.method == 'POST':
        report_type = request.POST.get('report_type')
        department_id = request.POST.get('department')

        if report_type == 'leave_requests':
            if department_id:
                department = Department.objects.get(id=department_id)
                users = User.objects.filter(department=department)
                leave_requests = LeaveRequest.objects.filter(user__in=users)
            context = {'leave_requests': leave_requests}

        elif report_type == 'salary_payments':
            if department_id:
                department = Department.objects.get(id=department_id)
                users = User.objects.filter(department=department)
                payrolls = Payroll.objects.filter(user__in=users)
            total_salaries = payrolls.aggregate(total=Sum('base_salary'))
            total_deductions = payrolls.aggregate(total=Sum('tax_deduction'))
            context = {
                'payrolls': payrolls,
                'total_salaries': total_salaries['total'],
                'total_deductions': total_deductions['total'],
            }

        elif report_type == 'attendance_summary':
            if department_id:
                department = Department.objects.get(id=department_id)
                users = User.objects.filter(department=department)
                attendances = Attendance.objects.filter(user__in=users)
            context = {'attendances': attendances}

        else:
            context = {}

    else:
        context = {}

    return render(request, 'reports/reports.html', {'departments': departments, **context})