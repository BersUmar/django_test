from django.db import models

# Create your models here.
class Breed(models.Model):
    title = models.CharField(max_length=50, verbose_name='название')
    overview = models.TextField(verbose_name='описание', blank=True, null=True)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'порода'
        verbose_name_plural = 'породы'

class Dog(models.Model):
    title = models.CharField(max_length=100, verbose_name='кличка')
    # breed = models.CharField(max_length=100, verbose_name='порода')
    breed = models.ForeignKey(Breed,on_delete=models.CASCADE, verbose_name='порода')
    image = models.ImageField(upload_to='dogs/', null=True, blank=True, verbose_name='фото')
    birthday = models.DateField(verbose_name='дата рождения')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'собака'
        verbose_name_plural = 'собаки'

