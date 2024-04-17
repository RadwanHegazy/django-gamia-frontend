from django.shortcuts import redirect
from django.views import View
from globals.decorators import login_required
from globals.request_manager import Action
from frontend.settings import MAIN_URL
from django.contrib import messages

class WithdrawView (View) : 
    
    @login_required
    def post(self,request,**kwargs) : 
        data = {
            'amount' : request.POST.get('amount',100)
        }

        action = Action(
            url=MAIN_URL + '/user/withdraw/',
            headers=kwargs['headers'],
            data=data
        )

        action.post()

        if not action.is_valid() : 
            messages.error(request,'حدث خطأ اثناء عملية السحب')
        else:
            messages.success(request,'تمت عملية السحب وسيتم ارسال الاموال الي محفظتك خلال 24 ساعة')
        
        return redirect('profile')

