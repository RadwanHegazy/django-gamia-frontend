from django.views import View
from django.shortcuts import render, redirect
from globals.decorators import login_required
from globals.request_manager import Action
from frontend.settings import MAIN_URL
from django.contrib import messages

class CreateGamiaView (View) :
    
    @login_required
    def get(self,request,**kwargs) : 
        return render(request,'gamia/create.html')
    
    @login_required
    def post(self,request,**kwargs) : 
        data = {**request.POST}
        action = Action(
            url=MAIN_URL + '/gamia/create/',
            headers=kwargs['headers'],
            data=data
        )

        action.post()

        if not action.is_valid() :
            messages.error(request,'an error accoured !')
            return redirect('create_gamia')
        
        gamia_id = action.json_data['id']
        return redirect('get_gamia',gamia_id)