from blog.models import Post
from django.contrib.auth.models import User
from django.utils import timezone


users = []
for i in range(3):
    username = f'user{i}'
    password = f'password{i}'
    if not User.objects.filter(username=username).exists():
        users.append(User.objects.create_user(username=username, password=password))


for user in users:
    for i in range(3):
        Post.objects.create(author=user,
                            title=f'Post {i} from {user.get_username()}',
                            text=f'This is post {i} from {user.get_username()}',
                            published_date=timezone.now())
