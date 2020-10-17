from django import forms
from .model import admin,Student


class  LoginForm(forms.Form):
    username=forms.CharField(max_length=100)
    password=forms.CharField(widget=forms.PasswordInput())

    def clean_user(self):
        username=self.cleaned_data.get("username")
        cleanpassword = self.cleaned_data.get("password")
        output="userdoesnotexist"
        studObject=Student.objects.filter(name=username,id=cleanpassword)
        adminObject=admin.objects.filter(username=username,password=cleanpassword)
        if(studObject):
            output="studlog"
        elif(adminObject):
            output="adminlog"
        else:
            output="wrongpassword"

        return output


