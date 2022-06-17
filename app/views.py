from django.http import Http404
from django.shortcuts import redirect, render
from django.contrib.auth import login,authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Profile,User,Project,Rate

from app.forms import RatingModelForm, UpdateUserProfileForm, UploadProjectModelForm, UserRegistrationForm

# Create your views here.
def home(request):
    project=Project.objects.all()
    return render(request,'index.html',{'project':project})

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

def project(request):
    # current_user = request.user
    project=Project.objects.all()
    return render(request,'project.html',{'project':project})
   

def project_detail(request,id):
    try:
        project = Project.objects.get(id=id)
        all = Rate.objects.filter(project=id)
        # print(all)
    except Exception as error:
        raise Http404()

    total = 0
    for i in all:
        total+=i.design
        total+=i.content
        total+=i.usability

    if total > 0:
        average = round(total/3,1)
    else:
        average =0

    if request.method == 'POST':
        form = RatingModelForm(request.POST)
        if form.is_valid():
            rate = form.save(commit=False)
            rate.profile_id=request.user.id
            rate.project=project
            rate.project_id=id
            rate.save()

        return redirect('project_detail',id)
    else:
        form = RatingModelForm()
    
    rates = Rate.objects.filter(project=id)
    design=[]
    usability = []
    content =[]

    for rate in rates:
        design.append(rate.design)
        usability.append(rate.usability)
        content.append(rate.content)

    if len(usability) > 0 and len(usability) <=10 or len(content) > 0 and len(content) <=10 or len(design) > 0 and len(design) <= 10:
        usability_average = round(sum(usability)/len(usability),1)
        design_average = round(sum(design)/len(design),1)
        content_average = round(sum(content)/len(content),1)

        total_average = round((usability_average+design_average+content_average)/3,1)

    else:
        usability_average = 0
        design_average = 0
        content_average = 0
        total_average = 0

    context = {
        'form': form,
        'project': project,
        'usability':usability_average,
        'design':design_average,
        'content':content_average,
        'total_average':total_average,
        'average':average,
    }
    return render(request, 'projectdetail.html',context)    


def project_new(request):
    current_user=request.user
    if request.method == "POST":
        form = UploadProjectModelForm(request.POST,request.FILES)
        if form.is_valid():
            new_project = form.save(commit=False)
            new_project.user = current_user
            new_project.save()
            messages.success(request, f'Your project has been uploaded!')   
            return redirect('project') 
        else:
            return render(request,'addproject.html',{'form':form})
    return render(request,'addproject.html')