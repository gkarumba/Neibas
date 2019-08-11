# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from .models import *
from django.contrib.auth.models import User
import datetime as dt
# Create your tests here.

class NeighbourHoodTest(TestCase):
    def setUp(self):
        self.Hood = Neighbourhood(name='Hood',location='4W', occupants=32, admin=User(id=1))
        
    def test_instance(self):
        self.assertTrue(isinstance(self.Hood), Neighbourhood)
        
    def tearDown(self):
        Neighbourhood.objects.all().delete()
        
    def test_save_method(self):
        self.Hood.save_neighbour()
        hood= Neighbourhood.objects.all()
        self.assertTrue(len(hood)>0)
        
    def test_delete_emthod(self):
        self.Hood.delete_neighbour('Hood')
        hood = Neighbourhood.objects.all()
        self.assertTrue(len(hood)==0)
        
class ProfileTest(TestCase):
    def setUp(self):
        self.Hood = Neighbourhood(name='Hood',location='4W', occupants=32, admin=User(id=1))
        self.profile =Profile(user=User(id=1),profilepic="img.png",bio="heloo world", neighbourhood = self.Hood, profile_email='hello@gmail.com')
        
    def test_instance(self):
        self.assertTrue(isinstance(self.profile,Profile))
        
    def test_initialization(self):
        self.assertEqual(self.profile.profilepic,'img.png')
        self.assertEqual(self.profile.bio,'heloo world')
        
    def test_save(self):
        self.Hood.save_neighbour()
        self.profile.save_profile()
        prof=Profile.objects.all()
        self.assertEqual(len(prof),0)
        
class BusinessTest(TestCase):
    def setUp(self):
        self.Hood = Neighbourhood(name='Hood',location='4W', occupants=32, admin=User(id=1))
        self.biz = Business(user=User(id=1), name='Health',neighbourhood=self.Hood,biz_email='hello@gmail.com',contact=0789567432)
        
    def test_instance(self):
        self.assertTrue(isinstance(self.biz),Business)
        
    def tearDown(self):
        Business.objects.all().delete()
        
    def test_save_method(self):
        self.biz.save_biz()
        biz = Business.objects.all()
        self.assertTrue(len(biz)>0)
    
    def test_delete_method(self):
        self.biz.delete_biz('biz')
        biz = Business.objects.all()
        self.assertTrue(len(biz)>0)
        
        