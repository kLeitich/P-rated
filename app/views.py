from django.shortcuts import redirect, render
from django.contrib.auth import login,authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Profile,User

from app.forms import UpdateUserProfileForm, UserRegistrationForm

# Create your views here.
def home(request):
    return render(request,'index.html')

def register_user(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()

            messages.success(request, f'Your account has been created. You can log in now!')    
            return redirect('login')
    else:
        form = UserRegistrationForm()

    context = {'form': form}
    return render(request, 'auth/register.html', context)


def profile(request):
    current_user = request.user
    user = User.objects.get(id = current_user.id)
    profile=Profile.filter_profile_by_id(user.id)
    # posts = Image.objects.filter(user = user.id)
    return render(request,'profile.html',{'profile':profile})


def update_profile(request,id):
    user = User.objects.get(id=id)
    profile = Profile.objects.get(user = user)
    if request.method == "POST":
            form = UpdateUserProfileForm(request.POST,request.FILES,instance=profile)
            if form.is_valid():
                form.save()
                return redirect('profile') 
            else:
                return render(request,'update_profile.html',{'form':form})
    else:        
        form = UpdateUserProfileForm(instance=profile)
    return render(request, 'update_profile.html', {'form':form})