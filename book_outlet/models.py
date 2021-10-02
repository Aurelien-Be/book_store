from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse 
from django.utils.text import slugify #transform a string to a slug
# Create your models here.

#we inherate a built in class in django 
class Book(models.Model):
    title = models.CharField(max_length=50)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    author = models.CharField(null=True, max_length=100)
    is_bestselling = models.NullBooleanField(default=False)
    #we can add a new slug attribute in order to have a nicer url than a simple number, for that django has a specific field
    slug = models.SlugField(default="", null=False, db_index=True) #harry-potter-1
    #add db_index improve the performance, as we use often this filter

    def get_absolute_url(self):
        return reverse("book-detail", args=[self.slug])

    #we can overwrite the save function, in order to set the value other than empty is set whenhever we save
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title) #the slug is added for all our models
        super().save(*args, **kwargs) #we make sur that the supermethod is called 



    def __str__(self):
        return f"{self.title} ({self.rating})"  #toconvertobjectsinareadableform
    
