from rest_framework import viewsets
from rest_framework import permissions
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import generics


from registration.serializers import *
from PandeminoApp.models import Account


@api_view(['POST'])
def registration_view(request):

    if request.method == 'POST':
        serializer = RegistrationSerlizer(data = request.data)

        data = {}
        if serializer.is_valid():
            account = serializer.save()
            data['response'] = "Sucsefully registred a new user"
            data['mail'] = account.mail
            data['username'] = account.username
        else:
            data = serializer.errors
        return Response(data)
