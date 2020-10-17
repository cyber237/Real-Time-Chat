from django.shortcuts import render,redirect
from data.model import admin
from django.http import HttpResponse,HttpResponseRedirect,HttpResponseNotFound
from django.urls import reverse
from django import forms
from json import loads,dumps
from data.forms import LoginForm


arr=[]


def login(request,data={}):
    if type(data)==type("string"):
        data=loads(data)
    return render(request, 'login/home.html', data)

def logging(request):
    username="not logged"
    if request.method== "POST":
        myloginform=LoginForm(request.POST)
        
        if myloginform.is_valid():
            if myloginform.clean_user()=="adminlog":
                request.session['username'] = request.POST['username']
                request.session['login'] = True
                request.session.set_expiry(0)
                arr.append(request.session.session_key)
                return HttpResponseRedirect(reverse('administrator'))
            elif myloginform.clean_user()=="studlog":
                request.session['id'] = request.POST['password']
                request.session['login'] = True
                request.session.set_expiry(0)
                arr.append(request.session.session_key)
                return HttpResponseRedirect(reverse('student'))
                
            elif myloginform.clean_user() == "wrongpassword":
                data1=dumps({"errormessage": myloginform.clean_user()})
                return redirect(login,data=data1)
            elif myloginform.clean_user() == "userdoesnotexist":
                data1 = dumps({"errormessage": myloginform.clean_user()})
                return redirect(login, data=data1)
            return HttpResponseNotFound()
        else:
            data1={"errormessage": myloginform.errors}
            return redirect(login, data=dumps(data1))
        
    else:
        return redirect(login)
                
def student(request):
    check=request.session.get('login',False)
    if check==True and request.session.session_key in arr:
        return render(request, 'student/student.html', {"id":  request.session.get('id', False)})
    else:
        return HttpResponseRedirect(reverse('login'))
    
def administrator(request):
    check=request.session.get('login',False)
    if check==True and request.session.session_key in arr:
        return render(request, 'administrator/admin.html', {"username":  request.session.get('username', False)})
    else:
        return HttpResponseRedirect(reverse('login'))
    