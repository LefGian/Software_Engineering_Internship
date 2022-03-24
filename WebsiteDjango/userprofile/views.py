from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .forms import UserUpdateForm
from django.contrib.auth import authenticate


# Create your views here.

@login_required
def userprofile(request):
    user = request.user
    form_user_update = UserUpdateForm(instance=user)
    print(f'username: {user.username} | userid: {user.id}')
    fehlermeldung_password1 = ''

    if request.method == 'POST':

        password1 = request.POST['jgu-password']
        password2 = request.POST['jgu-password-repeat']


        user_update_form_dict = {'csrfmiddlewaretoken': request.POST['csrfmiddlewaretoken'],
                                  'first_name': request.POST['jgu-vorname'],
                                  'last_name': request.POST['jgu-nachname'],
                                  'username': request.POST['jgu-username'],
                                }

        user_check = authenticate(request, username=user.username, password=password1)
        if user_check is None:
            form_user_update = UserUpdateForm(user_update_form_dict, instance=request.user)

            if password2:
                pass
                


        else:
            fehlermeldung_password1 = 'Password Wrong'


        if form_user_update.is_valid():
            form_user_update.save()
            
            return redirect('userprofile-userprofile')


        


    fehlermeldung_user_update = form_user_update.errors.as_data()
    print(fehlermeldung_user_update)
    fehlermeldung_user_update_str_arr = [fehlermeldung_password1]
    for key in fehlermeldung_user_update:
        for error_arr in fehlermeldung_user_update[key]:
            fehlermeldung_user_update_str_arr += error_arr

    print(fehlermeldung_user_update_str_arr)
    user_group = 'filler'
    context ={
        'form_user_update': form_user_update,
        'user': user,
        'user_group': user_group,
        'fehlermeldung_user_update_str_arr': fehlermeldung_user_update_str_arr,
    }
    return render(request, 'userprofile/nutzerprofil.html', context)