# from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render

# Create your views here.
from django.contrib.auth import login, authenticate
from django.views.generic import TemplateView, CreateView
from django.contrib.auth.views import LoginView as BaseLoginView
from django.contrib.auth.views import LogoutView as BaseLogoutView
from django.urls import reverse_lazy
from .forms import SignUpForm, LoginForm # ログインフォームをimport


class IndexView(TemplateView):
    """ ホームビュー """
    template_name = "index.html"

# @csrf_protect
class SignupView(CreateView):
    """ ユーザー登録用ビュー """
    form_class = SignUpForm # 作成した登録用フォームを設定
    template_name = "accounts/signup.html" 
    success_url = reverse_lazy("accounts:index") # ユーザー作成後のリダイレクト先ページ

    def form_valid(self, form):
        # ユーザー作成後にそのままログイン状態にする設定
        response = super().form_valid(form)
        account_id = form.cleaned_data.get("account_id")
        password = form.cleaned_data.get("password1")

        # ユーザーモデルに合わせて調整する
        # user = authenticate(self.request, account_id=account_id, password=password)
        user = authenticate(request=self.request, username=account_id, password=password)
        # user = authenticate(request=self.request, account_id=account_id, password=password)
        # user = authenticate(account_id=account_id, password=password)

        if user is not None:
            login(self.request, user)

        return response


# ログインビューを作成
# @csrf_protect
class LoginView(BaseLoginView):
    form_class = LoginForm
    template_name = "accounts/login.html"


# LogoutViewを追加
# @csrf_protect
class LogoutView(BaseLogoutView):
    success_url = reverse_lazy("accounts:index")





