from django.db import models
from datetime import datetime, timedelta
from django.contrib.auth.models import User
import random
import string

def al_slug(n=30):
    char = string.ascii_letters + string.digits
    slug= ""
    for i in range(n):
        slug += random.choice(char)
    return slug
class Categorie(models.Model):
    name= models.CharField(max_length=300)
    score = models.IntegerField(choices=[(1,"plutot inutile"),(2,"pas si utile"),(3,"assez utile"),(4,"Utile"),(5,"tres utile")], default=3)
    def __str__(self):
        return self.name
class Note(models.Model):
    title = models.CharField(max_length=300)
    slug = models.SlugField(max_length=300, default=al_slug(), unique=True)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    categorie = models.ForeignKey(Categorie,on_delete=models.PROTECT)
    body = models.TextField()
    date = models.DateTimeField(auto_now=True)
    status = models.BooleanField(choices=[(True,"actif"),(False,"expiré")], default=True)
    expiration = models.DateTimeField( default=datetime.now() + timedelta(days=10))
    def __str__(self):
        return self.title