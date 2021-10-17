from django.contrib import admin

from .models import Author, Book, Adress, Country

# Register your models here.


class BookAdmin(admin.ModelAdmin):
    #then we can have some fields only readable 
    #readonly_fields = ("slug") but we don't because we want a preview
    prepopulated_fields = {"slug" : ("title",)}
    list_filter = ("author", "rating")
    #to have columns 
    list_display = ("title","author", "rating")

admin.site.register(Book, BookAdmin)
admin.site.register(Author)
admin.site.register(Adress)
admin.site.register(Country)