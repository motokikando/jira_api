from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
import uuid

from django.db.models.fields import json

#プロフィール画像のパスの保存先の指定

def upload_avatar_path(instance, filename):
    #拡張子を定義
    ext = filename.split('.')[-1]
    return '/'.join(['avatars', str(instance.user_profile.id)+str('.')+str(ext)])


class Profile(models.Model):
    user_profile = models.OneToOneField(
        User, related_name='user_profile',
    on_delete=models.CASCADE
    )
    img = models.ImageField(blank=True, null=True, upload_to=upload_avatar_path)

    #作られたinstanceに対してdefaultでusernameの情報を返す
    def __str__(self):
        return self.user_profile.username



#Category
class Category(models.Model):
    item = models.CharField(max_length=100)

    #itemの文字の内容を返す
    def __str__(self):
        return self.item

#論文情報
class Thesis(models.Model):

    EVALUATION = (
        (1, '⭐️⭐️⭐️⭐️⭐️'),
        (2, '⭐️⭐️⭐️⭐️'),
        (3, '⭐️⭐️⭐️'),
        (4, '⭐️⭐️'),
        (5, '⭐️'),
    )
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    title = models.CharField(max_length=255, blank=True, null=True)
    authors = models.CharField(max_length=255, blank=True, null=True)
    year = models.PositiveIntegerField(blank=True, null=True)
    evaluation = models.IntegerField(blank=True, choices=EVALUATION)
    url = models.TextField(max_length=200, blank=False)
    introducer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='introducer')
    citaiton = models.TextField(blank=True)
    summary = models.TextField(blank=False)
    comment = models.TextField(blank=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title









