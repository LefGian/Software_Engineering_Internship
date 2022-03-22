from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm

# Create your views here.

def register(request):
    

    if request.method == 'POST':    # if we get a post request, initiate form to fillout
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account "{username}" has been created! Log In NOW!')
            return redirect('logout')
            
    else:   # else empy form
        form = UserRegisterForm()
    
    context = {
        'form': form,
    }
    return render(request, 'userapp/register.html', context)


@login_required
def profile(request):

    if request.method == 'POST':
        user_update_form = UserUpdateForm(request.POST, instance=request.user)
        if user_update_form.is_valid():
            user_update_form.save()
            messages.success(request, f'Your Info has been Updated')
            return redirect('profile')
    else:
        user_update_form = UserUpdateForm(instance=request.user)

    

    context = {
        'user_update_form': user_update_form,
    }
    return render(request, 'userapp/profile.html', context)
