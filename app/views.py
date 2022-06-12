from django.shortcuts import redirect, render
from django.contrib.auth import login
from django.contrib import messages
from app.forms import NewUserForm

# Create your views here.
def home(request):
    return render(request,'index.html')

def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("main:homepage")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render (request=request, template_name="auth/register.html", context={"register_form":form})