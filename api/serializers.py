from rest_framework import serializers
from .models import Category, Thesis, Profile
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username','password']
        extra_kwargs = {'password':{'write_only': True, 'required': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user



class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['id', 'user_profile', 'img']
        extra_kwargs = {'user_profile':{'read_only': True}}


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'item']


class ThesisSerializer(serializers.ModelSerializer):
    #各モデルから文字列の情報を取得
    category_item = serializers.ReadOnlyField(source='category.item', read_only = True)
    introducer_username = serializers.ReadOnlyField(source='introducer.username', read_only = True)
    evaluation_score = serializers.CharField(source='get_evaluation_display', read_only = True)
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M", read_only = True)
    updated_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M", read_only = True)

    class Meta:
        model = Thesis
        fields = ['id', 'title', 'authors', 'year', 'evaluation', 'evaluation_score', 'url', 'introducer', 'introducer_username', 'citaiton', 'summary', 'comment', 'category', 'category_item', 'created_at', 'updated_at']

        extra_kwargs = {'introducer':{'read_only': True}}
