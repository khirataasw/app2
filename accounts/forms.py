from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm  # 追加行
from django.contrib.auth import authenticate
# from accounts.models import CustomUser
from django.contrib.auth.models import User


# from .models import User


class SignUpForm(UserCreationForm):
     class Meta:
        model = User
        fields = (
            # "account_id",
            # # "username",
            # "email",
            # "first_name",
            # "last_name",
            # "birth_date",
            "username",
            "email",
            "first_name",
            "last_name",
            "password1",
            "password2",
        )
        


# ログインフォームを追加
class LoginForm(AuthenticationForm):
    #   class Meta:
         model = User
         fields = ['account_id', 'password']  # フィールドを指定




def clean(self):
    account_id = self.cleaned_data.get('account_id')
    password = self.cleaned_data.get('password')

    if account_id is not None and password:
       self.user_cache = authenticate(self.request, username=account_id, password=password)
       if self.user_cache is None:
        raise self.get_invalid_login_error()
    else:
        self.confirm_login_allowed(self.user_cache)

    return self.cleaned_data



