from typing import Any
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm


class UserCreateForm(UserCreationForm):
    
    class Meta:
        fields = ('username', 'email', 'password1', 'password2')
        #two passwords are for the confirmation of passwords
        model = get_user_model()

    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
        #this is for the custom labels for our form for each field
        self.fields['username'].label = 'Display Name'
        self.fields['email'].label = 'Email Address'
        
