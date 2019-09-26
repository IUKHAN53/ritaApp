from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from django.contrib import messages


def join(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        # print(form)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created succesfully!')
            return redirect('signin-page')
    else:
        form = UserRegisterForm()
    return render(request, 'users/join.html', {'form': form})
