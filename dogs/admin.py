from django.contrib import admin

from dogs.models import Dog, Breed
# Register your models here.

@admin.register(Breed)
class BreedAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title',)

@admin.register(Dog)
class DogAdmin(admin.ModelAdmin):
    list_display = ('title', 'breed',)