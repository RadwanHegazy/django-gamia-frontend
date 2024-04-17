from django.shortcuts import HttpResponse, render, redirect
from django.views import View
from globals.request_manager import Action
from frontend.settings import MAIN_URL
from django.contrib import messages

class RegisterView (View) : 

    def get(self,request,**kwargs) : 
        return render(request,'register.html')
    
    def post(self, request,**kwargs) : 

        data = {
            'email' : request.POST.get('email',None),
            'password' : request.POST.get('password',None),
            'full_name' : request.POST.get('full_name',None),
            'cash_phone' : f"+2{request.POST.get('mobile_cash',None)}",
        }

            
        action = Action(
            url=MAIN_URL + '/user/auth/register/',
            data=data
        )

        if 'picture' in request.FILES :
            action.files = {
                'picture' : request.FILES['picture']
            }

        action.post()

        if action.is_valid() :
            res = redirect('profile')
            res.set_cookie('user',action.json_data['access'])
            return res
        
        
        # for i in action.json_data.values():
        #     print(i)

        error_msg = ""
        error_msg = " and ".join([i[0] for i in action.json_data.values()])
        print(error_msg) 
        try : 
            messages.error(request,error_msg)
        except Exception : 
            messages.error(request,"invalid data enter")

        return redirect('register')