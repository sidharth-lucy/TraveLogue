from froala_editor import views
from unicodedata import name
from urllib.parse import urlparse
from django.urls import path,include
from . import views

urlpatterns = [
    path('froala_editor/',include('froala_editor.urls')),
    path('' , views.home , name='home'),
    path('signup' , views.UserSignUp , name= 'signup' ),
    path('login' , views.UserLogin , name='login'),
    path('logout' ,views.UserLogout , name='logout'),
    path('dashboard' , views.UserDashboard , name='dashboard'),
    path('userupdate' , views.Userupdate , name="userupdate") ,
    path('userpasswordchange' , views.UserPasswordChange , name= 'userpasswordchange'),
    path('post/<slug:slug>' , views.detailedPost , name='detailPost'),
    path('postcreation' , views.UserPostCreation , name='postcreation'),
    path('postdelete/<slug:slug>' , views.Userpostdelete , name='postdelete'),
    path('comment/<slug>' , views.UserComment , name= 'comment'),
    path('favourite' , views.addFavourite , name= 'addfavourite'),
    path('allfavpost' , views.allFavourite , name='allfavourite'),
    path('like-post' , views.Like_post , name='like-post'),
    path('userImageUpdate' , views.userImageUpdate , name= 'userImageUpdate'),
    path('Userportfolio/<int:userid>' , views.portfolio , name = 'portfolio'),
    path('follow' ,views.followUnfollow , name='follow'),
]
