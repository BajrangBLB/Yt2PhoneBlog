from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date
from ckeditor.fields import RichTextField

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('home')

class Post(models.Model):
    title = models.CharField(max_length=255)
    title_tag = models.CharField(max_length=255)

    header_image = models.ImageField(null=True, blank=True, upload_to="blog/images/")

    author = models.ForeignKey(User, on_delete = models.CASCADE)
    # body = models.TextField()
    body = RichTextField(blank=True, null= True, config_name='style2')
    pub_date = models.DateField(auto_now_add=True)
    category = models.CharField(max_length=255, default='coding')

    snippets = models.CharField(max_length=255, default='Click link above to read the blog Post')

    likes = models.ManyToManyField(User, related_name='blog_posts')

    def __str__(self):
        return self.title + " by " + str(self.author)

    def get_absolute_url(self):
        # return reverse('article_details', args=(str(self.id)))
        return reverse('home')
    
    def total_likes(self):
        return self.likes.count()

# TinyMust another rich text editor

class Comment(models.Model):
    post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s - %s' % (self.post.title, self.name)