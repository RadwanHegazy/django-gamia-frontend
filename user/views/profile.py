from django.shortcuts import HttpResponse, render, redirect
from django.views import View
from globals.decorators import login_required
from globals.request_manager import Action
from frontend.settings import MAIN_URL

class ProfileView (View) : 

    @login_required
    def get(self,request,**kwargs) : 
        context = {}
        action = Action(
            url=MAIN_URL+"/gamia/get/",
            headers=kwargs['headers']
        )
        action.get()
        context['list_data'] = action.json_data
        return render(request,'home.html',context=context)
    
