from rest_framework import serializers
from .models import User, Ground


class UserSerializers(serializers.ModelSerializer):

    profile = serializers.ImageField(max_length=None, use_url=True)

    class Meta:
        model = User
        fields = ('name', 'email', 'password', 'phone_no', 'dob', 'address', 'special_skill',
                  'fav_game', 'profile', 'score_or_prev_game')


class GroundSerializers(serializers.ModelSerializer):

    class Meta:
        model = Ground
        fields = ('name', 'location', 'available_status', 'price', 'rent_by', 'date', 'start_time', 'end_time', )
