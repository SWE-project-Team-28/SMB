from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import Profile_Update_Form, Registeration_Form
from smb_base.models import Question
from django.shortcuts import render, get_object_or_404
import sweetify

# Create your views here.
def register(request):

    form = UserCreationForm()
    
    if request.method == "POST":
        form = Registeration_Form(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            sweetify.success(request, f'Your Account Created Successfully', button='Ok',
                            timer=5000)
            return redirect('login')
    else:
        form = Registeration_Form()
    return render(request, 'smb_users/register.html', {'form': form})

@login_required
def profile(request):
        return render(request, 'smb_users/profile.html')
        
@login_required
def profile_update(request):
    if request.method == "POST":
        p_form = Profile_Update_Form(request.POST, request.FILES, instance=request.user.profile)
        if p_form.is_valid():
            p_form.save()
            sweetify.success(request, f'Your Profile Updated Successfully', button='Ok',
                            timer=5000)
            return redirect('profile')
    else:
        p_form = Profile_Update_Form(request.POST, request.FILES, instance=request.user.profile)
    data = {
        'p_form': p_form
    }
    return render(request, 'smb_users/profile_update.html', data)


def asked_by_user(request,username):
    user = get_object_or_404(User, username=username)
    questions = Question.objects.filter(user=user)
    context = {
        'user': user,
        'questions': questions,
    }
    return render(request,'smb_users/question_users.html', context)
