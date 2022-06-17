from django.test import TestCase
from .models import Profile,Project,Rate
from django.contrib.auth.models import User

# Create your tests here.
class TestProfile(TestCase):
    def setUp(self):
        self.user = User(id=1, username='joan',password='weuh')
        self.user.save()

    def test_instance(self):
        self.assertTrue(isinstance(self.user,User))

    def test_save_user(self):
        self.user.save()

    def test_delete_user(self):
        self.user.delete()

class TestProfile(TestCase):
    def setUp(self):
        self.user = User.objects.create(id=1, username='kevin',password='Moringaproject1')
        self.project = Project.objects.create(id=1, title='test project', image='media/projectimage/desktop.png',description='description',user=self.user, url='http://url.com')

    def test_instance(self):
        self.assertTrue(isinstance(self.project, Project))

    def test_save_project(self):
        self.project.save_project()
        project = Project.objects.all()
        self.assertTrue(len(project) > 0)

   

    def test_get_projects(self):
        self.project.save()
        projects = Project.all_projects()
        self.assertTrue(len(projects) > 0)


class TestRating(TestCase):
    def setUp(self):
        self.user = User.objects.create(id=2, username='Kevin',password='moringaproject1')
        self.project = Project.objects.create(id=2, title='test project', photo='media/projectimages/destop.png',description='description',user=self.user, url='http://url.com')
        self.rating = Rate.objects.create(id=2, design=5, usability=8, content=5, user=self.user, project=self.project)

    def test_instance(self):
        self.assertTrue(isinstance(self.rating, Rate))

    def test_save_rating(self):
        self.rating.save_rating()
        rating = Rate.objects.all()
        self.assertTrue(len(rating) > 0)

    def test_get_project_rating(self, id):
        self.rating.save()
        rating = Rate.get_ratings(project_id=id)
        self.assertTrue(len(rating) == 1)