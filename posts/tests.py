from django.test import TestCase
from django.contrib.auth.models import User
from .models import Post, Tag


class BlogTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser1', password='abc123')
        self.post = Post.objects.create(author=self.user, title='Blog title', body='Body content ...')

    def test_blog_content(self):
        post = Post.objects.get(id=self.post.id)
        self.assertEqual(f"{post.author}", 'testuser1')
        self.assertEqual(post.title, 'Blog title')
        self.assertEqual(post.body, 'Body content ...')

    def test_tags_model(self):
        t1 = Tag.objects.create(name="django")
        t2 = Tag.objects.create(name="api")
        self.post.tags.set([t1, t2])
        self.assertEqual(sorted([t.name for t in self.post.tags.all()]), ["api", "django"])