from django.shortcuts import HttpResponse, render, redirect
from django.views import View


class LogoutView (View) : 

    def get(self,request,**kwargs) : 
        res = redirect('login')
        res.delete_cookie('user')
        return res
    