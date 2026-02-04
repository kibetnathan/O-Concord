from rest_framework import serializers
from models import CustomUser, Profile
from datetime import date 

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'first_name', 'last_name', 'role', 'email']

class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)  # nested user info
    user_id = serializers.PrimaryKeyRelatedField(
        queryset=CustomUser.objects.all(),
        source='user',
        write_only=True
    )

    class Meta:
        model = Profile
        fields = [
            'id',
            'user',
            'user_id',
            'age',
            'DoB',
            'school',
            'workplace',
            'phone_number',
            'campus',
            'profile_pic'
        ]
    # Field-level validator for age
    def validate_age(self, value):
        if value < 0:
            raise serializers.ValidationError("Age cannot be negative")
        if value > 120:
            raise serializers.ValidationError("Age seems unrealistically high")
        return value

    # Field-level validator for DoB
    def validate_DoB(self, value):
        if value > date.today():
            raise serializers.ValidationError("Date of birth cannot be in the future")
        return value