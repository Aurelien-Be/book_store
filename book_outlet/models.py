from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db.models.deletion import CASCADE
from django.urls import reverse 
from django.utils.text import slugify #transform a string to a slug
# Create your models here.

class Country(models.Model):
    name = models.CharField(max_length=80)
    code = models.CharField(max_length=3)
    def __str__(self):
        return f"{self.name}"
    
    #to set how the Adress module is outputed
    class Meta:
        verbose_name_plural = "Countries"

class Adress(models.Model):
    street = models.CharField(max_length=80)
    postal_code = models.CharField(max_length=5)
    city = models.CharField(max_length=50)
     

    def __str__(self):
        return f"{self.street} {self.postal_code} {self.city}"
    
    #to set how the Adress module is outputed
    class Meta:
        verbose_name_plural = "Address Entries"


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    adress = models.OneToOneField(Adress, on_delete=CASCADE, null=True)
   

#to print the class as a string when needed :
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    def __str__(self): 
        return self.full_name() 
    
     

#we inherate a built in class in django 
class Book(models.Model):
    title = models.CharField(max_length=50)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True, related_name="books") #we point the preview class Author to make the relationship    # cascade = if author is deleted, then also the book in the data. 
    is_bestselling = models.BooleanField(default=False)
    #related_name allows to access to Author.books to query to all the books of an author
    #we can add a new slug attribute in order to have a nicer url than a simple number, for that django has a specific field
    slug = models.SlugField(default="", blank=True, null=False, db_index=True) #harry-potter-1
    #add db_index=True improve the performance, as we use often this filter
    #add editable = False to make impossible to edit in admin. But we cant do it if you use the preview feature
    #in order to make the slug field not mandatory in admin, we can add blank=True. Anyway, our function will edit the slug when we save
    published_countries = models.ManyToManyField(Country)

    def get_absolute_url(self):
        return reverse("book-detail", args=[self.slug])

    #we can overwrite the save function, in order to set the value other than empty is set whenhever we save
    #it is not useful with the prepopulated feature in admin, so I comment it
    #def save(self, *args, **kwargs):
    #    self.slug = slugify(self.title) #the slug is added for all our models
    #    super().save(*args, **kwargs) #we make sur that the supermethod is called 



    def __str__(self):
        return f"{self.title} ({self.rating})"  #toconvertobjectsinareadableform
    
