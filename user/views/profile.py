from django.shortcuts import HttpResponse, render, redirect
from django.views import View
from globals.decorators import login_required

class ProfileView (View) : 

    @login_required
    def get(self,request,**kwargs) : 
        return render(request,'home.html')
    
