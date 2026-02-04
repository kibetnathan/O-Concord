from rest_framework import serializers
from models import LeadershipTeam, AgeGroup, DiscipleshipGroup, RopesClass, ServingTeam, MinistryData
from django.conf import settings
from userapp.models import CustomUser

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'first_name', 'last_name', 'role']


class LeadershipTeamSerializer(serializers.ModelSerializer):
    members = serializers.PrimaryKeyRelatedField(
        many=True
    )

    class Meta:
        model = LeadershipTeam
        fields = ['id', 'name', 'description', 'members']


class AgeGroupSerializer(serializers.ModelSerializer):
    members = serializers.PrimaryKeyRelatedField(
        many=True
    )
    pastor = serializers.PrimaryKeyRelatedField(
        queryset=CustomUser.objects.all(),       allow_null=True
    )
    class Meta:
        model = AgeGroup
        fields = ['id', 'name', 'description', 'members', 'pastor']


class RopesClassSerializer(serializers.ModelSerializer):
    members = serializers.PrimaryKeyRelatedField(
        many=True
    )
    leader = serializers.PrimaryKeyRelatedField(
        queryset=CustomUser.objects.all(),
        allow_null=True
    )

    class Meta:
        model = RopesClass
        fields = ['id', 'leader', 'members']


class DiscipleshipGroupSerializer(serializers.ModelSerializer):
    members = serializers.PrimaryKeyRelatedField(
        many=True
    )
    leader = serializers.PrimaryKeyRelatedField(
        queryset=CustomUser.objects.all(),
        allow_null=True
    )

    class Meta:
        model = DiscipleshipGroup
        fields = ['id', 'name', 'description', 'leader' ,'members']


class ServingTeamSerializer(serializers.ModelSerializer):
    members = serializers.PrimaryKeyRelatedField(
        many=True
    )
    leader = serializers.PrimaryKeyRelatedField(
        queryset=CustomUser.objects.all(),
        allow_null=True
    )

    class Meta:
        model = ServingTeam
        fields = ['id', 'name', 'description', 'leader' ,'members']

        
class MinistryDataSerializer(serializers.ModelSerializer):
    # Nested user info
    user = UserSerializer(read_only=True)
    # Computed properties
    name = serializers.CharField(source='name', read_only=True)
    campus = serializers.CharField(source='campus', read_only=True)
    # Nested or IDs for relations
    dg = DiscipleshipGroupSerializer(read_only=True)
    department = ServingTeamSerializer(many=True, read_only=True)

    # For writable operations (POST/PUT), use PrimaryKeyRelatedField
    user_id = serializers.PrimaryKeyRelatedField(
        queryset=CustomUser.objects.all(), source='user', write_only=True
    )
    dg_id = serializers.PrimaryKeyRelatedField(
        queryset=DiscipleshipGroup.objects.all(), source='dg', write_only=True, allow_null=True
    )
    department_ids = serializers.PrimaryKeyRelatedField(
        queryset=ServingTeam.objects.all(),
        many=True,
        source='department',
        write_only=True,
        required=False
    )

    class Meta:
        model = MinistryData
        fields = [
            'id', 'user', 'user_id', 'name', 'campus', 'dg', 'dg_id', 'department', 'department_ids'
        ]