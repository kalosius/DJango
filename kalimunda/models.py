from django.db import models

# Create your models here.



class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Categories"
    

    
class Medicine(models.Model):

    name = models.CharField(max_length=20)
    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.IntegerField()

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Medicine"