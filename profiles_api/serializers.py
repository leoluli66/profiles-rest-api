from rest_framework import serializers

from profiles_api import models


class HelloSerializer(serializers.Serializer):
    """Serializes a name field for testing our APIView"""

    name = serializers.CharField(max_length=10)

# the way to use ModelSerializer is to use a meta class to configure the serializer to point
# to a specific model, which is the UerProfile model we created in the models.py
class UserProfileSerializer(serializers.ModelSerializer):
    """Serializes a user profile object"""

    class Meta:
        model = models.UserProfile
        fields = ('id', 'email', 'name', 'password')
        extra_kwargs = {
            'password': {
                'write_only': True, #will not be retrieved during http get
                'style': {'input_type': 'password'} # password * style
            }
        }

    # override the default create function provided by ModelSerializer
    def create(self, validated_data):
        """Create and return a new user"""
        user = models.UserProfile.objects.create_user(
            email=validated_data['email'],
            name=validated_data['name'],
            password=validated_data['password']
        )

        return user

#The password field requires some additional logic to hash the password before saving the update.
#We override the Django REST Framework ModelSerializer's update()
    def update(self, instance, validated_data):
        """Handle updating user account"""
        if 'password' in validated_data:
            password = validated_data.pop('password')
            instance.set_password(password) # save the psw as a hash

        return super().update(instance, validated_data)
