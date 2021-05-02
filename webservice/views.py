import json
from django.core import serializers
from django.http.response import JsonResponse
from webservice.models import Customer, Phone, PhoneDetails, PhoneRepairs, PhoneRequest, PhoneReviews, PhoneTransactions
from webservice.serializers import CustomerSerializer, PhoneDetailsSerializer, PhoneRepairsSerializer, PhoneRequestSerializer, PhoneReviewsSerializer, PhoneSerializer, PhoneTransactionsSerializer, UserSerializer
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from crum import get_current_user
from rest_framework.decorators import action
from rest_framework.response import Response
from django.contrib.auth.models import User, UserManager
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import CreateModelMixin
from django.contrib.auth import get_user_model
from .serializers import UserSerializer

# Create your views here.


class ProfileViewSet(viewsets.ViewSet):

    queryset = User.objects.all()
    serializer_class = UserSerializer

    @action(detail=False,  methods=['get'])
    def get_current_user(self, request, pk=None):
        user = User.objects.get(id=get_current_user().pk)
        user = UserSerializer(user)
        return Response(user.data)


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class PhoneViewSet(viewsets.ModelViewSet):
    queryset = Phone.objects.all()
    serializer_class = PhoneSerializer


class PhoneDetailsViewSet(viewsets.ModelViewSet):
    queryset = PhoneDetails.objects.all()
    serializer_class = PhoneDetailsSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['phone_id']


class PhoneTransactionsViewSet(viewsets.ModelViewSet):
    queryset = PhoneTransactions.objects.all()
    serializer_class = PhoneTransactionsSerializer

    @action(detail=False,  methods=['get'])
    def get_current_user_data(self, request, pk=None):
        data = PhoneTransactions.objects.filter(customer=get_current_user())
        serialized_qs = serializers.serialize(
            'json', data, use_natural_foreign_keys=True, use_natural_primary_keys=True)

        return JsonResponse(json.loads(serialized_qs), safe=False)


class PhoneRepairsViewSet(viewsets.ModelViewSet):
    queryset = PhoneRepairs.objects.all()
    serializer_class = PhoneRepairsSerializer

    @action(detail=False,  methods=['get'])
    def get_current_user_data(self, request, pk=None):
        data = PhoneRepairs.objects.filter(customer=get_current_user())
        serialized_qs = serializers.serialize(
            'json', data, use_natural_foreign_keys=True, use_natural_primary_keys=True)

        return JsonResponse(json.loads(serialized_qs), safe=False)


class PhoneReviewsViewSet(viewsets.ModelViewSet):
    queryset = PhoneReviews.objects.all()
    serializer_class = PhoneReviewsSerializer

    @action(detail=False,  methods=['get'])
    def get_current_user_data(self, request, pk=None):
        data = PhoneReviews.objects.filter(customer=get_current_user())
        serialized_qs = serializers.serialize(
            'json', data, use_natural_foreign_keys=True, use_natural_primary_keys=True)

        return JsonResponse(json.loads(serialized_qs), safe=False)


class PhoneRequestViewSet(viewsets.ModelViewSet):
    queryset = PhoneRequest.objects.all()
    serializer_class = PhoneRequestSerializer

    @action(detail=False,  methods=['get'])
    def get_current_user_data(self, request, pk=None):
        data = PhoneRequest.objects.filter(customer=get_current_user())
        serialized_qs = serializers.serialize(
            'json', data, use_natural_foreign_keys=True, use_natural_primary_keys=True)

        return JsonResponse(json.loads(serialized_qs), safe=False)


# class UserViewSet(viewsets.ViewSet):
#     permission_classes = []
#     authentication_classes = []
                                    
#     @action(detail=False,  methods=['post'])
#     def register(self, request, pk=None):
#         try:
#             serializer = UserSerializer(data=request.data)
#             if not serializer.is_valid():
#                 return serializer.errors
#             User.objects.create
#             user = User()
#             user.username=serializer.validated_data.get('username')
#             user.set_password(serializer.validated_data.get('password'))
#             user.first_name=serializer.validated_data.get(
#                 'first_name'), 
#             user.last_name=serializer.validated_data.get('last_name'), 
#             user.email=serializer.validated_data.get('email')
#             user.save()

#             return Response("User Created!")
#         except Exception as ex:
#             return Response(str(ex))

class CreateUserView(CreateModelMixin, GenericViewSet):
    permission_classes = []
    authentication_classes = []
    
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
