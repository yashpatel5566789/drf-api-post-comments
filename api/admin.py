from django.contrib import admin
from .models import Comment, Post

#class CommentInline(admin.StackedInline ):
#    model = Comment
 #   extra = 0

class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'timestamp', '__str__')
    #fields_list = ['id','title', 'description']
 #   fieldsets = [
 #       (None,  {'fields': fields_list}),
 #   ]
 #   inlines = [CommentInline]
    

admin.site.register(Post, PostAdmin)

