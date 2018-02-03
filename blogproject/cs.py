from blog.models import Category, Tag, Post
from django.utils import timezone
from django.contrib.auth.models import User

user = User.objects.get(username='root')
c = Category.objects.get(name='category test')
p = Post(title='title test', body='body test', created_time=timezone.now(), modified_time=timezone.now(), category=c, author=user)
p.save()