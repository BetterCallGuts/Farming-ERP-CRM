from django.db import models
from datetime import datetime




op = (
  ("Dry", "Dry"),
  ("Marigeable", "Marigeable"),
  ("Prgnent", "Prgnent"),
  ("Milk", "Milk")
)

class group(models.Model):
    pass


class report(models.Model):
    name = models.TextField
    data = models.DateTimeField(auto_now_add=datetime.now())
    
    
    def __str__(self):
        return self.name

class foodcategory(models.Model):
    name = models.CharField(max_length=250)
    
    
    def __str__(self):
        return self.name


class Warehouse(models.Model):
    name        = models.CharField(max_length=255)
    description = models.TextField(max_length=2000)
    
    
    def __str__(self):
        return self.name
    
    


class food(models.Model):
    # name  =  models.
    name = models.CharField(max_length=250 , null=True,blank=True)
    howmuch = models.IntegerField( null=True,blank=True) ;
    kgto4ekarah = models.IntegerField(null=True,blank=True);
    category    = models.ForeignKey(foodcategory, on_delete=models.SET_NULL, null=True)
    
    def get_how_much_4ekarah(self):
        return self.howmuch / kgto4ekarah
    def __str__(self):
        return self.name




class shekara(models.Model):
    food  = models.ForeignKey(food, on_delete=models.SET_NULL, null=True)
    
    def __str__(self):
        return self.name
    
    
    
class cow(models.Model):
    name         = models.CharField( max_length=250, default=""          ,null=True,blank=True);
    age          = models.IntegerField(default=""                        ,null=True,blank=True);
    state        = models.CharField(choices=op,   max_length=250,                       null=True,blank=True);
    is_male      = models.BooleanField(default=False                     ,null=True,blank=True);


    food         = models.ForeignKey(food, on_delete=models.SET_NULL     ,null=True,blank=True);
    logs         = models.ForeignKey(report, on_delete=models.SET_NULL   ,null=True,blank=True);
    def __str__(self):
        return self.name



class milk(models.Model):
    how_much   = models.IntegerField(null=True,blank=True)

    cowownmilk = models.ForeignKey(cow, on_delete   = models.SET_NULL , null=True, blank=True)  
    logs       = models.ForeignKey(report, on_delete= models.SET_NULL , null=True, blank=True)
    
    def __str__(self):
        return f"The cow:{self.cowownmilk.name}, howmuch:{self.how_much}"
    


