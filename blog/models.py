from django.db import models
from django.urls import reverse
from django.core.validators import MinLengthValidator

# Create your models here.



class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True) # it validates that the text entered is a valid email address


    def __str__(self):
        return self.first_name + " " + self.last_name
    
class Tag(models.Model):
    caption = models.CharField(max_length=50)

    def __str__(self):
        return self.caption
    
    

class Post(models.Model):
    title = models.CharField(max_length=150)
    excerpt = models.CharField(max_length=200)
    image = models.CharField(max_length=50)
    # image = models.ImageField()
    date = models.DateField(auto_now = True) #auto_now = True will update the date every time the object is saved
    slug = models.SlugField(unique=True, db_index=True) #db_index=True will create an index for the slug field in the database for faster queries. its set to true by defualt 
    content = models.TextField(validators=[MinLengthValidator(10)])
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True, related_name="posts") # if the author is deleted, the posts will not be deleted, but the author field will be set to null
    tags = models.ManyToManyField(Tag)


    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("post-details", args=[self.slug])
        

