from django.db import models
from crum import get_current_user

# Create your models here.

class Customer(models.Model):
    name = models.TextField()
    sex = models.CharField(max_length=1)
    phone_no = models.CharField(max_length=20)
    email = models.EmailField()
    address = models.TextField()

class Phone(models.Model):
    name = models.CharField(max_length=50)
    brand = models.CharField(max_length=50)

    def natural_key(self):
        return self.name

class PhoneDetails(models.Model):
    phone = models.ForeignKey(Phone, on_delete=models.CASCADE)
    screen_size = models.CharField(max_length=50)
    dimension = models.CharField(max_length=50)
    price = models.BigIntegerField()
    front_camera = models.CharField(max_length=50)
    operating_system = models.CharField(max_length=50)
    storage = models.CharField(max_length=50)
    ram = models.PositiveIntegerField()
    battery_capacity = models.PositiveIntegerField()
    battery_type = models.CharField(max_length=50)

class PhoneTransactions(models.Model):
    phone = models.ForeignKey(Phone, on_delete=models.DO_NOTHING)
    customer = models.ForeignKey('auth.user', default= get_current_user, on_delete=models.DO_NOTHING)
    price = models.IntegerField()
    transaction_date = models.DateTimeField()


class PhoneRepairs(models.Model):
    phone = models.ForeignKey(Phone, on_delete=models.DO_NOTHING)
    customer = models.ForeignKey('auth.user', default= get_current_user, on_delete=models.DO_NOTHING)
    price = models.IntegerField()
    repair_date = models.DateTimeField()
    remarks = models.TextField()

class PhoneReviews(models.Model):
    phone = models.ForeignKey(Phone, on_delete=models.DO_NOTHING)
    customer =  models.ForeignKey('auth.user', default= get_current_user, on_delete=models.DO_NOTHING)
    review = models.TextField()
    stars = models.PositiveIntegerField()

class PhoneRequest(models.Model):
    phone_name = models.TextField()
    phone_details = models.TextField()
    customer = models.ForeignKey('auth.user', default= get_current_user, on_delete=models.DO_NOTHING)

