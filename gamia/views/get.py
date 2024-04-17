from django.views import View
from django.shortcuts import render, redirect
from globals.decorators import login_required
from globals.request_manager import Action
from frontend.settings import MAIN_URL
from django.http import Http404

class GetGamiaView (View) :
    
    @login_required
    def get(self,request,gamia_id,**kwargs) : 

        action = Action(
            url= MAIN_URL + f'/gamia/get/{gamia_id}/',
            headers=kwargs['headers']
        )

        action.get()

        if not action.is_valid() : 
            raise Http404(request)

        context = action.json_data

        return render(request,'gamia/view.html',context=context)
    
