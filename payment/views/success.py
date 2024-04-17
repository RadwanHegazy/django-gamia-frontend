from django.views import View
from globals.request_manager import Action
from django.shortcuts import redirect
from django.contrib import messages
from frontend.settings import MAIN_URL
from django.http import HttpResponseBadRequest

class SuccessView (View) : 

    def get(self,request,payment_id,user_token,**kwargs):

        action = Action(
            url=MAIN_URL + f'/payment/{payment_id}/success/',
            headers={
                'Authorization' : f'Bearer {user_token}'
            }
        )

        action.get()

        if not action.is_valid() : 
            raise HttpResponseBadRequest(request)


        messages.success(request,'تم شحن حسابك بنجاح')
        
        res = redirect('profile')
        res.set_cookie('user',user_token)
        return res