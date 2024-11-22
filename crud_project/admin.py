from django.contrib import admin
from crud_project.models import Author, BlogPost

# Register your models here.

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    pass


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):  
    list_display = ("title", "content", "created_on", "author")  
    list_editable = ("content",) 
    list_display_links = ("title",)  
    search_fields = ("title", "content")  
    list_filter = ("created_on",)  
    list_per_page = 10  
