from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now=False, auto_now_add=False,default=timezone.now)
    authors = models.ForeignKey(User, on_delete=models.CASCADE,null = True, blank = True)
    shit = models.CharField(null=True,blank=True, max_length=50)
    def __str__(self):
        return self.title

class EnvVaribles(models.Model):
    moneyratio_a = models.FloatField(default=1,null=True)
    moneyratio_b = models.FloatField(default=1,null=True)
    moneyratio_c = models.FloatField(default=1,null=True)
    country_a_taxes = models.FloatField(default=1,null=True)
    country_b_taxes = models.FloatField(default=1,null=True)
    country_c_taxes = models.FloatField(default=1,null=True)
    bidding_a1 = models.FloatField(default=1,null=True)
    bidding_a2 = models.FloatField(default=1,null=True)
    bidding_a3 = models.FloatField(default=1,null=True)
    bidding_b1 = models.FloatField(default=1,null=True)
    bidding_b2 = models.FloatField(default=1,null=True)
    bidding_b3 = models.FloatField(default=1,null=True)
    bidding_c1 = models.FloatField(default=1,null=True)
    bidding_c2 = models.FloatField(default=1,null=True)
    bidding_c3 = models.FloatField(default=1,null=True)
 

    def __str__(self):
        return "environment varibles"

class testmodel(models.Model):

    活该 = models.FloatField(default=1,null=True)
