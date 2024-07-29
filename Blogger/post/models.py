from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=225)

    def __str__(self):
        return '%s' % (self.name)

class Post(models.Model):
    title = models.CharField(max_length=225)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    body = models.TextField()
    published_on = models.DateField(auto_now_add=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    likes = models.ManyToManyField(User, related_name='blog_post')

    def __str__(self):
        return '%s - %s' % (self.title,self.author)

    def total_likes(self):
        return self.likes.count()

    def get_absolute_url(self):
        return reverse('singlepost',args=(str(self.id)))

class comment(models.Model):
    post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    body = models.TextField()
    date_added = models.DateField(auto_now_add=True)

    def __str__(self):
        return '%s - %s' % (self.post.title, self.user)