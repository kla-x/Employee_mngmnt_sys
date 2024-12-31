from django.shortcuts import render,redirect


from django.contrib.auth  import login, authenticate,  logout
from django.contrib.auth.decorators import login_required 

from  .forms import UserRegistrationForm
from .models import User 

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            if user.is_approved:
                login(request, user)
                return redirect('dashboard')
            else:
                # User is not approved
                return render(request, 'accounts/waiting_approval.html')
    return render(request, 'accounts/login.html')

def register_view(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)  # Don't save the user yet
            user.is_approved = False  # Set is_approved to False
            user.save()  # Now save the user
            return render(request, 'accounts/waiting_approval.html')
    else:
        form = UserRegistrationForm()
    return render(request, 'accounts/register.html', {'form': form})

@login_required
def dashboard(request):
    return render(request, 'dashboard.html')


@login_required
def user_logout(request):
   logout(request)

   return redirect('login')