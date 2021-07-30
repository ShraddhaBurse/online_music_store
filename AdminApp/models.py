from django.db import models


# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=20)

    def __str__(self):
        return self.category_name
 
    class Meta:
        db_table = "Category"        

class Song(models.Model):
    sname= models.CharField(max_length=20)
    artist= models.CharField(max_length=20)
    movie= models.CharField(max_length=20)
    imageurl= models.ImageField(upload_to='images')
    audio_file = models.FileField()
    duration=models.CharField(max_length=20)
    Category = models.ForeignKey(Category,on_delete=models.CASCADE) 
    
    def __str__(self):
        return self.sname

    class Meta:
        db_table = "Song"