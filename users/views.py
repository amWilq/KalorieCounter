from django.shortcuts import render, redirect
from  django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm, GoalUpdateForm, UserGoalUpdateForm

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Konto zostało stworzone dla {username}')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})



@login_required
def profile (requset):
    if requset.method == 'POST':
        u_form = UserUpdateForm(requset.POST, instance=requset.user) #Wypełnia pole aktualnymi danymi
        p_form = ProfileUpdateForm(requset.POST,
                                   requset.FILES,
                                   instance=requset.user.profile) #Wypełnia pole aktualnymi danymi

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=requset.user)  # Wypełnia pole aktualnymi danymi
        p_form = ProfileUpdateForm(instance=requset.user.profile)  # Wypełnia pole aktualnymi danymi
    context = {
        'u_form':u_form,
        'p_form':p_form
    }
    return render(requset, 'users/profile.html', context)


@login_required
def cele (requset):
    if requset.method == 'POST':
        p_form = GoalUpdateForm(requset.POST,requset.FILES,instance=requset.user.profile)
        if p_form.is_valid():
            p_form.save()
            return redirect('home')
    else:
        p_form = GoalUpdateForm(instance=requset.user.profile)
    context = {
        'p_form':p_form
    }
    return render(requset, 'users/cele.html', context)