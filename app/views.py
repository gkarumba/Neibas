# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from .models import *
from .forms import *


# Create your views here.
@login_required(login_url='/accounts/login/')
def index(request):
    try: 
        current_user = request.user
        profile = Profile.objects.get(user=current_user)
    except ObjectDoesNotExist:
        return redirect('edit')
    return render(request,'index.html')

def profile(request):
    current_user =request.user
    profile=Profile.objects.get(user=current_user)
    
    return render(request,'profile.html',{'profile':profile})

def edit_profile(request):
    current_user=request.user
    if request.method == 'POST':
        form = ProfileForm(request.POST,request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = current_user
            profile.save()
        return HttpResponseRedirect('/')
    else:
        form = ProfileForm()
    return render(request,'edit_profile.html',{"form":form})
            