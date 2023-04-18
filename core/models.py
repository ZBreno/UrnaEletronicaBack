from django.db import models

# Create your models here.
class Candidate(models.Model):
    name = models.CharField(max_length=50, verbose_name='nome')
    political_party = models.CharField(max_length=50, verbose_name='partido')
    number = models.IntegerField(verbose_name='numero')
    quantity_votes = models.IntegerField(verbose_name='votos totais')
    
    def __str__(self):
        return self.name