from django import forms
from django.contrib.auth.models import User
from .models import Account

#フォームクラス
class AccountForm(forms.ModelForm):
    #パスワード入力: 非表示
    password = forms.CharField(widget=forms.PasswordInput(), label='パスワード')
    
    class Meta():
        #ユーザ認証
        model = User
        #フィールド指定
        fields = ['username', 'email', 'password']
        #フィールド名指定
        labels = {'username':"ユーザーID", 'email':"メール"}
        
class AddAccountForm(forms.ModelForm):
    class Meta():
        #モデルクラスの指定 AccountFormではユーザー認証によるフィールドの定義、AddAccountFormではDjangoのユーザー認証システム(user)で指定されいないフィールドを定義した。
        model = Account
        fields = ('last_name', 'first_name', 'account_image',)
        labels = {'last_name':'苗字','first_name':'名前','account_image':'写真',}