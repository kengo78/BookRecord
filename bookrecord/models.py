from django.db import models
from django.contrib.auth.models import User
# Create your models here.

#ユーザーアカウントのモデルクラス
class Account(models.Model):
    
    #ユーザー認証のインスタンス
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    #追加フィールド
    last_name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    account_image = models.ImageField(upload_to="profile_pics",blank=True)
    
    def __str__(self):
        return self.user.username
    
class Record(models.Model):
    
    title = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    author = models.CharField(max_length=30)
    content = models.TextField(null=True, blank=True)
    end_data = models.DateField()#defaultは当日
    