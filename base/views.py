from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import *
from .emails import *


class RegisterApi(APIView):

    def post(self, request):
            data = request.data
            serializer = UserSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                send_otp_via_mail(serializer.data['email'])
                return Response({
                    'status': 200,
                    'message': 'registration successfully check mail',
                    'data': serializer.data,
                })

            return Response({
                'status': 400,
                'message': 'something went wrong',
                'data': serializer.errors,
            })


class VerifyOTP(APIView):
    def post(self, request):
        data = request.data
        serializer = VerifyAccountSerializer(data = data)

        if serializer.is_valid():
            email = serializer.data['email']
            otp = serializer.data['otp']

            user = User.objects.filter(email = email)
            if not user.exists():
                return Response({
                    'status': 400,
                    'message': 'something went wrong',
                    'data': 'invalid email',
                })

            if user[0].otp != otp:
                return Response({
                    'status': 400,
                    'message': 'something went wrong',
                    'data': 'invalid otp',
                })
            user = user.first()
            user.is_verified = True
            user.save()

            return Response({
                'status': 200,
                'message': 'account verified',
                'data': {},
            })

        return Response({
            'status': 400,
            'message': 'something went wrong',
            'data': serializer.errors,
        })

