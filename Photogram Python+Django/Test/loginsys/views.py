from django.contrib.auth.models import User
from django.shortcuts import render_to_response, redirect, render
from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm
from django.core.context_processors import csrf

from loginsys.models import RegForm


def login(request):
    args = {}
    args.update(csrf(request))
    if request.POST:
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        if user is not None and user.is_active:
            auth.login(request, user)
            return redirect('/')
        else:
            args['login_error'] = "User doesn't exist"
            return render_to_response('loginsys/login.html', args)
    else:
        return render_to_response('loginsys/login.html', args)

def logout(request):
    auth.logout(request)
    return redirect("/")

#def registration(request):
#    args = {}
#    args.update(csrf(request))
#    args['form'] = UserCreationForm()
#    if request.POST:
#        newuser_form = UserCreationForm(request.POST)
#        if newuser_form.is_valid():
#            newuser_form.save()
#            newuser = auth.authenticate(username=newuser_form.cleaned_data['username'], password=newuser_form.cleaned_data['password2'])
#            auth.login(request, newuser)
#            return redirect('/')
#        else:
#            args['form'] = newuser_form
#    return render_to_response('loginsys/registration.html', args)

def registration(request):
    if request.method == 'POST':
        form = RegForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            repeat_password = request.POST['repeat_password']
            try:
                check = User.objects.get(username=username)
            except:
                if password==repeat_password:
                    user = User.objects.create_user(username=username, password=password)
                    user.save()
                    user = auth.authenticate(username=username, password=password)
                    auth.login(request, user)
                    return redirect('/')
                else:
                    error = "Passwords should be similar"
                    return render_to_response('loginsys/registration.html', {'form': form, 'error': error})
            if check:
                error = "Nickname has already taken"
                return render_to_response('loginsys/registration.html', {'form': form, 'error': error})
            #else:
            #    if password1==password2:
            #        user = User.objects.create_user(username=username, password=password1)
            #        user.save()
            #        user = auth.authenticate(username=username, password=password1)
            #        auth.login(request, user)
            #        return redirect('/')

            #user = auth.authenticate(username=username, password=password1)
            #if user is not None or not (password1 == password2):
            #    user = User.objects.create_user(username=username, password=password1)
            #    user.save()
            #    user = auth.authenticate(username=username, password=password1)
            #    auth.login(request, user)
            #    return redirect('/')
            #else:
            #    error = "There is a problem"
            #    return render_to_response('loginsys/registration.html', {'form': form, 'error': error})
    else:
        form = RegForm()

    return render(request, 'loginsys/registration.html', {'form': form})