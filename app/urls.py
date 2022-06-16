from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.urls import  path
from django.contrib.auth import views as auth_views


urlpatterns=[
    path('',views.home,name='home'),
    path('register/',views.register_user,name = 'register'),
    path('login/', auth_views.LoginView.as_view(template_name='auth/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='auth/login.html'), name='logout'),
    path('profile',views.profile,name='profile'),
    path('update_profile/<int:id>',views.update_profile,name='update_profile'),
    path('project',views.project,name='project'),
    # path('project/<int:id>',views.project_detail,name='project_detail'),
    # path('project/<int:id>/update',views.project_update,name='project_update'),
    # path('project/<int:id>/delete',views.project_delete,name='project_delete'),
    path('project/new',views.project_new,name='project_new'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)