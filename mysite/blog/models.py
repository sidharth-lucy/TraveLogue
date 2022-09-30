
from distutils.command.upload import upload
from email.policy import default

from django.db import models
from froala_editor.fields import FroalaField
from django.contrib.auth.models import User
from PIL import Image

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=40)
    slug = models.SlugField(unique=True)
    date = models.DateField(auto_now=True)
    image= models.ImageField(upload_to='image')
    exerpt= models.TextField(max_length=150)
    # content= models.TextField()
    content= FroalaField()
    like = models.IntegerField(default=0)

    author= models.ForeignKey(User,on_delete=models.CASCADE,related_name='author')
    tag = models.ManyToManyField("Tags",related_name='tag')

    def __str__(self):
        return self.title



class Tags(models.Model):
    batch = models.CharField(max_length=20)

    def __str__(self):
        return self.batch


class Comments(models.Model):
    comment_text = models.TextField(max_length=300)
    post= models.ForeignKey(Post ,on_delete=models.CASCADE ,related_name='post')
    author= models.ForeignKey(User ,default=None, on_delete=models.CASCADE , related_name='commentauthor')

    # def __str__(self):
    #     return self.post.title


class UserImage(models.Model):
    uimage= models.ImageField(upload_to='userimage' , default=None)
    aboutme = models.TextField(max_length=1300 , default='Please Write somthing about yourself.')
    designation = models.CharField(default='Unknown' ,max_length=50)
    youtube = models.URLField(max_length=300 ,default='https://www.youtube.com/')
    twiter  = models.URLField(max_length=300 ,default='https://twitter.com/')
    instagram = models.URLField(max_length=300 ,default='https://www.instagram.com/')
    author= models.OneToOneField(User , on_delete=models.CASCADE , related_name='userimg')

    follower= models.IntegerField(default=0)
    following= models.IntegerField(default=0)

    def __str__(self):
        return self.author.username



    # def save(self):
    #     super().save()

    #     img = Image.open(self.image.path) # Open image

    #     # resize image
    #     if img.height > 300 or img.width > 300:
    #         output_size = (300, 300)
    #         img.thumbnail(output_size) # Resize image
    #         img.save(self.image.path) # Save it again and override the larger image



class LikesPost(models.Model):
    postId = models.IntegerField()
    username = models.CharField(max_length=200)



    def __str__(self):
        return self.username

class Follower(models.Model):
    user = models.CharField(max_length=100)
    follower=models.CharField(max_length=100) 

    def __str__(self):
        return self.user 