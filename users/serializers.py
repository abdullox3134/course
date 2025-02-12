from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from .models import CustomUser, Profile


class UserRegisterSerializer(serializers.ModelSerializer):
    password1 = serializers.CharField(write_only=True, required=True)
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = CustomUser
        fields = ['phone', 'name', 'lastname', 'password1', 'password2']

    def validate(self, attrs):
        """
        Validate that password1 and password2 are the same.
        """
        if attrs['password1'] != attrs['password2']:
            raise serializers.ValidationError("Passwords do not match.")

        # Validate password using Django's built-in validators
        validate_password(attrs['password1'])

        return attrs

    def create(self, validated_data):
        # Remove password2 as it's not part of the model
        validated_data.pop('password2')
        password = validated_data.pop('password1')  # Get the first password

        # `name` va `lastname` borligini tekshiramiz
        name = validated_data.get('name', '').strip()
        lastname = validated_data.get('lastname', '').strip()

        if not name or not lastname:
            raise serializers.ValidationError({"detail": "Name va lastname bo‘sh bo‘lishi mumkin emas"})

        # `full_name` ni avtomatik o‘rnatamiz
        validated_data['full_name'] = f"{name} {lastname}"

        # Create the user with the rest of the validated data
        user = CustomUser.objects.create(**validated_data)

        # Set the password
        user.set_password(password)
        user.save()

        return user


class ProfileSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source='user.full_name', read_only=True)
    class Meta:
        model = Profile
        fields = ['id', 'user', 'bio', 'birth_date', 'location']
        read_only_fields = ['user']