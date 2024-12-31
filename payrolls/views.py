from django.shortcuts import render, get_object_or_404
from django.http import Http404

# Create your views here.

from django.contrib.auth.decorators import login_required
from .models import Payroll

# @login_required
# def payroll_view(request):
#     payroll = Payroll.objects.get(user=request.user)
#     return render(request, 'payrolls/payroll.html', {'payroll': payroll})

@login_required
def doesnt_exist(request):
    return render(request, 'payrolls/not_exist.html' )

def payroll_view(request):
    try:
        payroll = get_object_or_404(Payroll, user=request.user)
        return render(request, 'payrolls/payroll.html', {'payroll': payroll})
    except Http404:
        # Handle the case where request.user does not exist
        return render(request, 'payrolls/not_exist.html')

    

def PagenotFound404(request, exception):
    return render(request, '404.html/', {}, status=404)