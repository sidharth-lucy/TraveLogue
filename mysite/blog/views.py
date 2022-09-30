from django.core.exceptions import ObjectDoesNotExist

from django.http import JsonResponse
from django.shortcuts import render, HttpResponseRedirect 
from django.urls import reverse

from datetime import datetime

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group,User
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UserChangeForm, \
     SetPasswordForm , PasswordChangeForm 
from django.contrib.auth import login,logout,authenticate,update_session_auth_hash
from django.contrib import messages

from .models import Post, Comments, Tags ,LikesPost ,UserImage ,Follower
from .forms import UserSignupForm , UserUpdateForm , UserPostForm ,UserCommentform,userImageForm

# Create your views here.




@login_required(login_url='login')
def followUnfollow(request):
    if request.method=='POST':
        follower_user= request.user
        follower_user_img = follower_user.userimg
        # print(follower_user_img.aboutme)
        user= User.objects.get(username= request.POST['user']) 
        user_img = user.userimg
        # print(user_img.aboutme)
        
        follo_list = Follower.objects.filter(follower=follower_user.username ,user= user.username)
        
        # print(follo_list)
        if len(follo_list)==0:
            new_foll = Follower(follower= follower_user.username ,user= user.username)
            new_foll.save()

            user_img.follower =user_img.follower+1 
            follower_user_img.following=follower_user_img.following + 1
            user_img.save()
            follower_user_img.save()
        else:
            follo_list[0].delete()
            
            user_img.follower = user_img.follower-1
            follower_user_img.following= follower_user_img.following-1 
            user_img.save()
            follower_user_img.save()
        return HttpResponseRedirect(reverse('portfolio' ,args=[user.id]))
    else:
        return HttpResponseRedirect(reverse('home'))





@login_required(login_url='login')
def portfolio(request,userid):
    user = User.objects.get(id = userid)
    userdetail = UserImage.objects.get(author= user)
    return render(request, 'blog/portfolio.html' , {
        'user':user,
        'userdetail':userdetail,
    })




def userImageUpdate(request):
    if request.user.is_authenticated:
        
        if request.method =='POST':
            try:
                if request.user.userimg:
                    fm = userImageForm(request.POST,request.FILES, instance=request.user.userimg)
                    if fm.is_valid():
                        img= fm.save(commit=False)
                        img.author = request.user
                        img.save()
                        return HttpResponseRedirect(reverse('dashboard'))
            except ObjectDoesNotExist:
                fm = userImageForm(request.POST,request.FILES)
                if fm.is_valid():
                    img= fm.save(commit=False)
                    img.author = request.user
                    img.save()
                    return HttpResponseRedirect(reverse('dashboard'))
        else:
            fm = userImageForm(instance=request.user.userimg)
        return render(request ,'blog/uploadimage.html' ,{
            'form':fm,
        })
    else:
        return HttpResponseRedirect(reverse('login'))


def allFavourite(request): 
    postid= request.session.get('favourite')
    if postid==None:
        all_fav_post=[]
    else:
        all_fav_post = Post.objects.filter(id__in =postid)

    have_fav= False
    if len(all_fav_post)>0:
        have_fav=True
    
    return render(request , 'blog/allfavouritepost.html' ,{
        'all_fav_post':all_fav_post,
        'have_fav':have_fav,
    })


def addFavourite(request):
    if request.user.is_authenticated:
        fav_post_id = int(request.POST['fav_post'])
        fav= request.session.get('favourite')
        if fav==None:
            fav= []
        if fav_post_id not in fav:
            fav.append(fav_post_id)
        else:
            fav.remove(fav_post_id)
        
        request.session['favourite'] = fav
        favpost= Post.objects.get(id=fav_post_id)
        return HttpResponseRedirect(reverse('detailPost' , args=[favpost.slug]))
    else:
        return HttpResponseRedirect(reverse('login'))



def isFav(request, id):
    is_fav = False
    fav = request.session.get('favourite')
    if fav !=None:
        if id in fav:
            is_fav=True
    return is_fav



def UserComment(request , slug):
    if request.user.is_authenticated:
        if request.method=="POST":
            fm = UserCommentform(request.POST)
            if fm.is_valid():
                targetpost= Post.objects.get(slug=slug)
                comment= fm.save(commit=False)
                comment.post= targetpost
                comment.author= request.user
                comment.save() 
                
        return HttpResponseRedirect(reverse('detailPost' , args=[slug]))

    else:
        return HttpResponseRedirect(reverse('login'))


@login_required(login_url='login')
def Like_post(request):
    if request.method =='GET':
        username= request.user.username
        post_id = request.GET.get('post_id')

        like_filter = LikesPost.objects.filter(postId=post_id , username= username).first()
        post =  Post.objects.get(id= post_id)
        total_like= 0
        if like_filter==None:
            newlike = LikesPost.objects.create(postId=post_id,username=username)
            newlike.save()
            post.like = post.like+1
            post.save()
            total_like= post.like

        else:
            like_filter.delete()
            post.like = post.like - 1
            post.save()
            total_like= post.like
        
        data={
            'likes':total_like
        }

    return JsonResponse(data)




# @login_required(login_url='login')
# def Like_post(request):
#     username= request.user.username
#     post_id = request.GET.get('post_id')

#     like_filter = LikesPost.objects.filter(postId=post_id , username= username).first()
#     post =  Post.objects.get(id= post_id)
#     if like_filter==None:
#         newlike = LikesPost.objects.create(postId=post_id,username=username)
#         newlike.save()
#         post.like = post.like+1
#         post.save()

#     else:
#         like_filter.delete()
#         post.like = post.like - 1
#         post.save()

#     return HttpResponseRedirect('/')

def Userpostdelete(request , slug):
    if request.user.is_authenticated:
        if request.method =="POST":
            post = Post.objects.get(slug=slug)
            if request.user== post.author:
                post.delete()
        
        return HttpResponseRedirect(reverse('dashboard'))

    else:
        return HttpResponseRedirect(reverse('login'))


def detailedPost(request , slug):
    post= Post.objects.get(slug=slug)
    tag= post.tag.all()
    is_fav = isFav(request,post.id)
    print(is_fav)
    comment= post.post.all()
    fm= UserCommentform()
    return render(request , 'blog/postdetail.html' , {
        'post':post,
        'tag':tag, 
        'form':fm,
        'comment':comment,
        'is_fav':is_fav,
    })


def slugCreation(arr):
    a = ''
    for i in range(len(arr)):
        if arr[i].isalnum() or arr[i]==' ':
            a+=arr[i]

    s= a.split()
    t= datetime.now()
    sl= str(t)
    sl= sl.replace(':' ,'-').replace(' ','-').replace('.','-')
    sl= '-'.join(s) +sl 
    return sl 


def UserPostCreation(request):
    if request.user.is_authenticated:
        if request.method =='POST':
        
            fm = UserPostForm(request.POST ,request.FILES)
            temp= request.POST['title']
            if fm.is_valid():
            
                new_post = fm.save(commit=False)
                new_post.author = request.user
                new_post.slug= slugCreation(str(temp))
                new_post.save()
                fm.save_m2m()
                
                messages.success(request , 'Post Created!')
                return HttpResponseRedirect('dashboard')

        else:
            fm = UserPostForm()

        return render(request , 'blog/postcreation.html' ,{
            'form':fm , 
        })

    else:
        return HttpResponseRedirect('login')




def UserDashboard(request):
    if request.user.is_authenticated:
        user_name = request.user
        # img= user_name.userimg.uimage
        all_post = request.user.author.all().order_by('-date')
        return render(request , 'blog/dashboard.html' , {
            'uname':user_name,
            'post':all_post,
        
        } )
    else:
        return HttpResponseRedirect('login')


def home(request):
    all_post= Post.objects.all().order_by('-date')
    have_post = True 
    if len(all_post)==0:
        have_post=False
    return render(request , 'blog/home.html' , {
        'post':all_post,
        'have_post':have_post,
    })

def UserSignUp(request):
    if request.method=='POST':
        
        fm = UserSignupForm(request.POST)
        uname = request.POST['username']
        existingUser = User.objects.filter(username=uname).first()
        if existingUser:
            return render(request , 'blog/signup.html' , {
                'form':fm, 'uname':'This username already exist!'
            })
        else:    
            if fm.is_valid():
                usr= fm.save()
                grp= Group.objects.get(name='blogger')
                usr.groups.add(grp)

                ###############
                # user_detail = UserImage(author= usr,uimage='https://www.dropbox.com/s/cbqm3pn7ae3gq3f/user-icon-jpg-21.jpg?dl=1')
                user_detail = UserImage(author= usr , uimage ='userimage/defaultuser.jpg')
                
                user_detail.save()
                ##########

                return HttpResponseRedirect('/')
    else:
        fm = UserSignupForm()
    return render(request , 'blog/signup.html' , {
        'form':fm,
    })

def Userupdate(request):
    if request.user.is_authenticated:
        if request.method=='POST':
            fm = UserUpdateForm(request.POST , instance= request.user)
            if fm.is_valid():
                fm.save()
                messages.success(request , 'Profile Updated Successfuly')
                return HttpResponseRedirect('dashboard')
        else:
            fm= UserUpdateForm(instance = request.user)
        return render(request , 'blog/userupdate.html' , {
            'form':fm ,
        })
    else:
        return HttpResponseRedirect('login')


def UserLogin(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('/')
    if request.method=='POST':
        fm = AuthenticationForm(request=request ,data= request.POST)
        if fm.is_valid():
            uname= fm.cleaned_data['username']
            upass= fm.cleaned_data['password']
            user= authenticate(username= uname , password= upass)
            if user is not None:
                login(request ,user)
                messages.success(request , 'Logged In successfully !')
                return HttpResponseRedirect('/')
    else:
        fm= AuthenticationForm()
        return render(request , 'blog/login.html' , {
            'form':fm
        })
    

def UserLogout(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request , 'Logged Out Successfuly !!')
        return HttpResponseRedirect('/')
    
    else:
        return HttpResponseRedirect('/')


def UserPasswordChange(request):
    if request.user.is_authenticated:
        if request.method=='POST':
            fm = PasswordChangeForm(user= request.user , data= request.POST)
            if fm.is_valid():
                fm.save()
                messages.success(request , "Password changed Successfuly!!!")
                update_session_auth_hash(request , fm.user)
                return HttpResponseRedirect('dashboard')
        else:
            fm = PasswordChangeForm(user= request.user)
        return render(request , 'blog/passwordupdate.html' ,{
            'form':fm, 
        })
    else:
        return HttpResponseRedirect('login')