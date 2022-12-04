from rest_framework.serializers import ModelSerializer

from apps.auto_parks.serializers import AutoParkSerializer

from .models import UserModel


class UserSerializer(ModelSerializer):
    auto_parks = AutoParkSerializer(many=True, read_only=True)

    class Meta:
        model = UserModel
        fields = (
            'id', 'email', 'password', 'is_active', 'crated_at', 'update_at', 'is_superuser', 'is_staff', 'last_login',
            'auto_parks'
        )
        read_only_fields = (
            'id', 'email', 'crated_at', 'update_at', 'is_superuser', 'is_staff', 'last_login')
        extra_kwargs = {
            'password': {
                'write_only': True
            }
        }

    def create(self, validated_data):
        return UserModel.objects.create_user(**validated_data)
