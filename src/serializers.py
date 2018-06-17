from backend.src.models import User
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('firstname', 'lastname', 'email', 'phone', 'password')

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return User.objects.create(**validated_data)

    def update(self, user, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        user.firstname = validated_data.get('firstname', user.firstname)
        user.lastname = validated_data.get('lastname', user.lastname)
        user.email = validated_data.get('email', user.email)
        user.phone = validated_data.get('phone', user.phone)
        user.password = validated_data.get('password', user.password)
        user.save()
        return user

