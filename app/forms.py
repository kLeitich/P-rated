from django import forms

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from app.models import Profile, Project,Rate


# Create your forms here.

class UserRegistrationForm(UserCreationForm):
   

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class UpdateUserProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('fname','lname','bio','ppic','phone','twitter','facebook','linkedin')

class UploadProjectModelForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ('image','description','title','url')

class RatingModelForm(forms.ModelForm):
    class Meta:
        model = Rate
        fields = ('design','usability','content')