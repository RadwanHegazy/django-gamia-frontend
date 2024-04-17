from django.shortcuts import redirect
from django.views import View
from globals.decorators import login_required
from globals.request_manager import Action
from frontend.settings import MAIN_URL
from django.contrib import messages

class ChargeView (View) : 
    
    @login_required
    def post(self,request,**kwargs) : 
        data = {
            'amount' : request.POST.get('amount',100)
        }

        action = Action(
            url=MAIN_URL + '/user/charge/',
            headers=kwargs['headers'],
            data=data
        )

        action.post()

        if not action.is_valid() : 
            messages.error(request,'حدث خطأ اثناء عملية الشحن')
            return redirect('profile')
        
        response = action.json_data

        return redirect(response['payment_link'])

