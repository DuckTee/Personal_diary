from django.shortcuts import redirect, render
from django.contrib.auth import login
from .forms import UserRegistrationForm

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('diary:entry_list')
    else:
        form = UserRegistrationForm()

    return render(request, 'users/register.html', {'form': form})
