# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Neighbourhood(models.Model):
    '''
    Model for the neighbourhoods
    '''
    name = models.CharField(max_length =255)
    location = models.CharField(max_length=255)
    occupants = models.IntegerField()
    admin = models.ForeignKey(User,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
    
    def save_neighbour(self):
        self.save()
        
    @classmethod
    def delete_neighbour(cls,neiba):
        cls.objects.filter(name=neiba).delete()
        
    @classmethod
    def update_neighbour(cls,neiba,new_neiba):
        cls.objects.filte(name=neiba).update(name=new_neiba)
        
    @classmethod
    def update_occupants(cls,neiba,new_occ):
        cls.objects.filter(name=neiba).update(occupants=new_occ)
        
    @classmethod find_neiba(cls,name):
        result = cls.objects.filter(name__icontains=name)
        return result

class Profile(models.Model):
    