from django.contrib.auth.models import User
from webservice.models import Customer, Phone, PhoneDetails, PhoneRepairs, PhoneRequest, PhoneReviews, PhoneTransactions
from rest_framework import serializers

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'

class PhoneSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    class Meta:
        model = Phone
        fields = '__all__'

class PhoneDetailsSerializer(serializers.ModelSerializer):
    phone = PhoneSerializer(data='phone_viewset')
    class Meta:
        model = PhoneDetails
        fields = '__all__'
        

class PhoneTransactionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhoneTransactions
        fields = '__all__'

class PhoneRepairsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhoneRepairs
        fields = '__all__'

class PhoneReviewsSerializer(serializers.ModelSerializer):
    phone = PhoneSerializer(source='phone_viewset')
    class Meta:
        model = PhoneReviews
        fields = '__all__'

class PhoneRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhoneRequest
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):        
    class Meta:
        model = User
        fields = '__all__'
                                                                                                                                                        
