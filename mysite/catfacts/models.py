from django.db import models

# Create your models here.
class CatFact(models.Model):
    fact = models.CharField('fact',max_length = 512) # 512 characters

    def __str__(self):
        return self.fact