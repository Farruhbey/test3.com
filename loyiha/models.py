from django.db import models

class Talabalar(models.Model):
    ismi = models.CharField(max_length = 100)
    familiyasi = models.CharField(max_length = 100)
    otasi_ismi = models.CharField(max_length = 100)
    yoshi = models.IntegerField(null=True)
    biladigan_dasturlash_tili = models.CharField(max_length = 100, null=True)
    rasmi = models.ImageField()
    qachon_oqigan = models.DateField(auto_now_add = True)
    
    

    def __str__(self) -> str:
        return f'{self.ismi} {self.familiyasi} {self.otasi_ismi}'

class Loyiha(models.Model):
    nomi = models.CharField(max_length = 400)
    sisilka = models.CharField(max_length = 400)
    rasmi = models.ImageField()
    talaba = models.ForeignKey(Talabalar, related_name="loyihalar", on_delete = models.CASCADE)

    def __str__(self) -> str:
        return self.nomi

       

      
# Create your models here.
