from rest_framework import serializers
from .models import *


class IdentificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Identification
        fields = "__all__"


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 4
        model = User
        exclude = ('password', 'clone_password')


class CategoryLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryLocation
        fields = "__all__"


class SubCategoryLocationSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 1
        model = SubCategoryLocation
        fields = "__all__"


class HotelAmenitySerializer(serializers.ModelSerializer):
    class Meta:
        model = HotelAmenity
        fields = "__all__"


class HotelSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 2
        model = Hotel
        exclude = ('hotel_bank_number', 'user')


class RoomTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomType
        fields = "__all__"


class RoomSerializer(serializers.ModelSerializer):
    hotel = HotelSerializer()

    class Meta:
        model = Room
        fields = "__all__"


class RoomReservationSerializer(serializers.ModelSerializer):
    hotel = HotelSerializer()
    room = RoomSerializer()

    class Meta:
        model = RoomReservation
        fields = '__all__'


class CarForRentSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarForRent
        fields = '__all__'


class ImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Images
        fields = '__all__'


class CarRentalSerializer(serializers.ModelSerializer):
    hotel = HotelSerializer()
    car = CarForRentSerializer()

    class Meta:
        model = CarRental
        fields = '__all__'


class RestaurantAmenitySerializer(serializers.ModelSerializer):
    class Meta:
        model = RestaurantAmenity
        fields = '__all__'


class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 4
        model = Restaurant
        fields = '__all__'


class MealCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = MealCategory
        fields = '__all__'


class MealSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meal
        fields = '__all__'


class TableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Table
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'


class TableReservationSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 4
        model = TableReservation
        fields = '__all__'


class DeliverySerializer(serializers.ModelSerializer):
    class Meta:
        depth = 4
        model = Delivery
        fields = '__all__'


class PaymentCheckSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentCheck
        fields = "__all__"


class CheckIdentifySerializer(serializers.ModelSerializer):
    class Meta:
        model = CheckIdentify
        fields = '__all__'


class RoomImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomImages
        fields = '__all__'


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 4
        model = Contact
        fields = '__all__'


class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 4
        model = Notification
        fields = '__all__'

