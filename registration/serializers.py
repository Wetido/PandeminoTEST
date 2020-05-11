from django.contrib.auth.models import User, Group
from PandeminoApp.models import Account
from rest_framework import serializers


class RegistrationSerlizer(serializers.ModelSerializer):

    password2 = serializers.CharField( style = {'input_type' : 'password'}, write_only=True)

    class Meta:
        model = Account
        fields = ['username', 'password', 'mail', 'password2']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def save(self):
        account = Account(
            email = self.validated_data['mail'],
            username = self.validated_data['username'],

        )
        password = self.validated_data['password']
        password2 = self.validated_data['password2']

        if password != password2:
            raise serializer.ValidationEroor({'password': 'Passwords must match'})
        #account.set_password(password)
        #account.save()

        return account
