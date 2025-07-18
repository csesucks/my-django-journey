from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
def register(request):
    if request.method == 'POST':
        form =UserRegisterForm(request.POST)  # Fixed '=' instead of '-'
        if form.is_valid():  # Fixed 'is_valod()' typo
            form.save()  # Save the user
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has benn created! You are now able to log in')
            return redirect('blog-home')  # Make sure 'blog-home' exists in urls.py
    else:
        form = UserRegisterForm()
    
    return render(request, 'users/register.html', {'form': form})

@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, 'Your profile has been updated!')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'users/profile.html', context)