from django.contrib import admin

# Register your models here.
from .models import Post, Author, Tag

class PostAdmin(admin.ModelAdmin):
    list_filter = ("author", "tags", "date") # adds a filter sidebar to the admin page
    list_display = ("title", "date", "author") # adds a column for the title, date, and author in the admin page
    prepopulated_fields = {"slug": ("title",)} # adds a slug field to the admin page

admin.site.register(Post, PostAdmin)
admin.site.register(Author)
admin.site.register(Tag)