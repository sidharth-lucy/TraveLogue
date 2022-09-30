from django.contrib import admin



from .models import Comments,Post,Tags,UserImage,LikesPost,Follower
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display= ('title','date','author',)
    list_filter =('title','tag','author',)
    # prepopulated_fields ={'slug':('title','tag',)}

class CommentAdmin(admin.ModelAdmin):
    list_display = ('post','author',)

admin.site.register(Comments,CommentAdmin)
admin.site.register(Post,PostAdmin)
admin.site.register(Tags)
admin.site.register(UserImage)
admin.site.register(LikesPost)
admin.site.register(Follower)