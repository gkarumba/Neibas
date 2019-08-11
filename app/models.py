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
    '''
    Model for user profiles
    '''
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    profilepic = models.ImageField(upload_to='profiles/')
    bio = models.CharField(max_length=255)
    neighbourhood = models.ForeignKey(Neighbourhood, on_delete=models.CASCADE)
    profile_email = models.CharField(max_length=255)
    
    def __str__(self):
        return self.bio
    
    def save_profile(self):
        self.save()
        
    @classmethod
    def delete_profile(cls,username):
        cls.objects.filter(user=username).delete()
        
class Business(models.Model):
    '''
    Model for the businesses
    '''
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    neibourhood = models.ForeignKey(Neighbourhood,on_delete=models.CASCADE)
    biz_email = models.EmailField()
    contact = models.IntegerField()
    
    def __str__(self):
        return self.name
    
    def save_biz(self):
        self.save()
    
    @classmethod
    def delete_biz(cls,name):
        cls.objects.filter(name=name).delete()
        
    @classmethod
    def update_biz(cls,biz,email,contact):
        cls.objects.filter(name=biz).update(biz_email=email, contact=contact)
        
    @classmethod
    def find_biz(cls,term):
        result = cls.objects.filter(name__icontains=term)
        return result