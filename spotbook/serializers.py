from django.contrib.auth import authenticate
from rest_framework import serializers

class LoginSerializer(serializers.Serializer):
    email = serializers.CharField(
        label="email",
        write_only=True
    )
    password = serializers.CharField(
        label="password",
        style={'input_type': 'password'},
        trim_whitespace=False,
        write_only=True
    )

    def validate(self, attrs):
        # get email, password from request
        email = attrs.get('email')
        password = attrs.get('password')

        if email and password:
            # Try to authenticate the user using Django auth framework.
            user = authenticate(
                request=self.context.get('request'),
                email=email, password=password
            )
            if not user:
                # If we don't have a regular user, raise a ValidationError
                msg = 'Access denied: wrong email or password.'
                raise serializers.ValidationError(msg, code='authorization')
        else:
            msg = 'Both "email" and "password" are required.'
            raise serializers.ValidationError(msg, code='authorization')
        # We have a valid user, put it in the serializer's validated_data.
        # It will be used in the view.
        attrs['user'] = user
        return attrs
