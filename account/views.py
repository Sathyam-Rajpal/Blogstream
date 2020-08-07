from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import SignupForm, UserUpdateForm, ProfileUpdateForm
# Create your views here.

# View for user registration, we make a form
# two request methods 'Get' and 'post'
def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            # flash messages that pop for 1 time untill refresh
            messages.success(request, f'Account Created - Login to start sharing!')
            return redirect('login')
    else:
        form = SignupForm()
        
    context = {
        'form':form,
        }
    #by default looks into templates directory
    return render(request,'account/signup.html',context)

@login_required
def profile(request):
    # We keep the current data filled in the forms, so we put instance = user {the variable for active user}
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance = request.user)
        # The request.FILES is necessary as we have image data too in the p_form
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance = request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            # flash messages that pop for 1 time untill refresh
            messages.success(request, f'Profile Information Updated')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance = request.user)
        p_form = ProfileUpdateForm(instance = request.user.profile)

    context = {
        'u_form':u_form,
        'p_form':p_form,
        }
    return render(request,'account/profile.html',context)

    