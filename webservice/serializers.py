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
    phone_obj = PhoneSerializer(source='phone_viewset', read_only=True)
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
        write_only_fields = ('password',)
        read_only_fields = ('id',)

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )

        user.set_password(validated_data['password'])
        user.save()

        return user                                                                                                                        
