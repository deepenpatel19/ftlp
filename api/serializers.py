from rest_framework import serializers
from .models import User


class UserSerializers(serializers.ModelSerializer):

    profile = serializers.ImageField(max_length=None, use_url=True)

    class Meta:
        model = User
        fields = ('name', 'email', 'password', 'phone_no', 'dob', 'address', 'special_skill',
                  'fav_game', 'profile', 'score_or_prev_game')
