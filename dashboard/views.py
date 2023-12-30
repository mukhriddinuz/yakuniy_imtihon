from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.generics import ListAPIView, ListCreateAPIView, DestroyAPIView, UpdateAPIView
from .models import *
from .serializers import *


"""START CRUD CHECK IDENTIFY"""


class CreateCheckIdentify(ListCreateAPIView):
    queryset = CheckIdentify.objects.all()
    serializer_class = CheckIdentifySerializer


class DeleteCheckIdentify(DestroyAPIView):
    queryset = CheckIdentify.objects.all()
    serializer_class = CheckIdentifySerializer


@api_view(['GET'])
def get_check_identify(request, pk):
    try:
        check_identify = CheckIdentify.objects.get(pk=pk)
        ser = CheckIdentifySerializer(check_identify)
        data = ser.data
    except:
        status = 404
        message = 'Object not found'
        data = {
            'status': status,
            'message': message
        }
    return Response(data)


"""END CRUD CHECK IDENTIFY"""

"""START CRUD IDENTIFICATION"""


@api_view(['POST'])
def create_identification(request):
    try:
        user = request.GET.get('user_id')
        usr = User.objects.get(user_id=user)
        ser = IdentificationSerializer(data=request.data, partial=True)
        if ser.is_valid():
            user.approved = True
            user.save()
            ser.save()
            return Response(ser.data)
    except Exception as err:
        return {'message': str(err)}


"""END CRUD IDENTIFICATION """

"""START CRUD CATEGORY LOCATION"""


class CreateCategoryLocation(ListCreateAPIView):
    queryset = CategoryLocation.objects.all()
    serializer_class = CategoryLocationSerializer


class GetCategoryLocation(ListAPIView):
    queryset = CategoryLocation.objects.all()
    serializer_class = CategoryLocationSerializer


class UpdateCategoryLocation(UpdateAPIView):
    queryset = CategoryLocation.objects.all()
    serializer_class = CategoryLocationSerializer


class DeleteCategoryLocation(DestroyAPIView):
    queryset = CategoryLocation.objects.all()
    serializer_class = CategoryLocationSerializer


"""END CRUD CATEGORY LOCATION"""

"""STATR CRUD SUB CATEGORY LOCATION"""


class CreateSubCategoryLocation(ListCreateAPIView):
    queryset = SubCategoryLocation.objects.all()
    serializer_class = SubCategoryLocationSerializer


class GetSubCategoryLocation(ListAPIView):
    queryset = SubCategoryLocation.objects.all()
    serializer_class = SubCategoryLocationSerializer


class UpdateSubCategoryLocation(UpdateAPIView):
    queryset = SubCategoryLocation.objects.all()
    serializer_class = SubCategoryLocationSerializer


class DeleteSubCategoryLocation(DestroyAPIView):
    queryset = SubCategoryLocation.objects.all()
    serializer_class = SubCategoryLocationSerializer


"""END CRUD SUB CATEGORY LOCATION"""

"""STATR CRUD HotelAmenity"""


class CreateHotelAmenity(ListCreateAPIView):
    queryset = HotelAmenity.objects.all()
    serializer_class = HotelAmenitySerializer


class GetHotelAmenity(ListAPIView):
    queryset = HotelAmenity.objects.all()
    serializer_class = HotelAmenitySerializer


class UpdateHotelAmenity(UpdateAPIView):
    queryset = HotelAmenity.objects.all()
    serializer_class = HotelAmenitySerializer


class DeleteHotelAmenity(DestroyAPIView):
    queryset = HotelAmenity.objects.all()
    serializer_class = HotelAmenitySerializer


"""END CRUD HotelAmenity"""

"""CREATE CRUD HOTEL"""


class CreateHotel(ListCreateAPIView):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer

    def create(self, request, *args, **kwargs):
        try:
            user_id = request.data.get('user')
            user = User.objects.get(pk=user_id)
            if user.limit >= len(Hotel.objects.filter(user=user)) and user.limit > 0:
                ser = self.get_serializer(data=request.data)
                ser.is_valid(raise_exception=True)
                hotel = ser.save()
                images = request.data.getlist('images', [])
                amenities = self.request.data.getlist('amenities', [])
                for amenity in amenities:
                    hotel.amenities.add(amenity)
                for i in images:
                    img = Images.objects.create(image=i)
                    hotel.image.add(img)
                headers = self.get_success_headers(ser.data)
                data = ser.data
            else:
                data = {
                    'status': 403,
                    'message': 'The limit is set'
                }
        except Exception as err:
            data = {'message': str(err)}
        return Response(data)


class EditHotel(UpdateAPIView):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer

    def edit(self, request, *args, **kwargs):
        try:
            ser = self.get_serializer(data=request.data)
            ser.is_valid(raise_exception=True)
            instance = self.get_object()
            instance.name = ser.validated_data.get('name', instance.name)
            instance.hotel_bank_number = ser.validated_data.get('hotel_bank_number', instance.hotel_bank_number)
            instance.sub_category_location_id = ser.validated_data.get('sub_category_location', instance.sub_category_location_id)
            instance.lat = ser.validated_data.get('lat', instance.lat)
            instance.lot = ser.validated_data.get('lot', instance.lot)
            instance.location_text = ser.validated_data.get('location_text', instance.location_text)
            instance.description = ser.validated_data.get('description', instance.description)
            instance.call_centre = ser.validated_data.get('call_centre', instance.call_centre)
            instance.number_rooms = ser.validated_data.get('number_rooms', instance.number_rooms)
            instance.amenities.set(ser.validated_data.getlist('amenities', instance.amenities.all()))
            instance.car_rental = ser.validated_data.get('car_rental', instance.car_rental)
            instance.room_reservation = ser.validated_data.get('room_reservation', instance.room_reservation)
            instance.restaurant_and_cafe = ser.validated_data.get('restaurant_and_cafe', instance.restaurant_and_cafe)
            instance.shopping = ser.validated_data.get('shopping', instance.shopping)
            instance.cleaning_room_service = ser.validated_data.get('cleaning_room_service', instance.cleaning_room_service)
            images = ser.validated_data.getlist('images', [])
            for i in images:
                img = Images.objects.create(image=i)
                instance.image.add(img)
            instance.save()
            ser = self.get_serializer(instance)
            data = ser.data
        except Exception as err:
            data = {'message': str(err)}
        return Response(data)


class GetAllHotel(ListAPIView):
    queryset = Hotel
    serializer_class = HotelSerializer


class DeleteHotel(DestroyAPIView):
    queryset = Hotel
    serializer_class = HotelSerializer


"""END CRUD HOTEL"""

"""STATR CRUD RoomType"""


class CreateRoomType(ListCreateAPIView):
    queryset = RoomType.objects.all()
    serializer_class = RoomTypeSerializer


class GetAllRoomType(ListAPIView):
    queryset = RoomType.objects.all()
    serializer_class = RoomTypeSerializer


class UpdateRoomType(UpdateAPIView):
    queryset = RoomType.objects.all()
    serializer_class = RoomTypeSerializer


class DeleteRoomType(DestroyAPIView):
    queryset = RoomType.objects.all()
    serializer_class = RoomTypeSerializer


"""END CRUD RoomType"""


"""STAR CRUD ROOM """


class RoomCreateView(ListCreateAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer

    def create(self, serializer):
        room_instance = serializer.save()
        room_image_data = self.request.data.getlist('room_images', [])
        room_image_serializer = RoomImagesSerializer(data=room_image_data, many=True)
        if room_image_serializer.is_valid():
            room_image_serializer.save(room=room_instance)
        else:
            room_instance.delete()
            raise serializers.ValidationError({'error': 'Invalid room images data'})


class EditRoom(UpdateAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer

    def edit(self, serializer):
        room_instance = serializer.save()
        room_image_data = self.request.data.getlist('room_images', [])
        room_image_serializer = RoomImagesSerializer(data=room_image_data, many=True)
        if room_image_serializer.is_valid():
            room_image_serializer.save(room=room_instance)
        else:
            raise serializers.ValidationError({'error': 'Invalid room images data'})


class DeleteRoom(DestroyAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer


"""END CRUD ROOM"""

""" START CRUD RoomReservation"""


@api_view(['POST'])
def create_room_reservation(request):
    try:
        ser = RoomReservationSerializer(data=request.data)
        ser.is_valid(raise_exception=True)
        reservations = RoomReservation.objects.filter(
            room=ser.validated_data['room'],
            to_date__gt=ser.validated_data['from_date'],
            from_date__lt=ser.validated_data['to_date']
        )

        if reservations.exists():
            data = {'status': 403, 'message': 'This room is already booked for the specified time period'}

        ser.save()
        data = ser.data
    except Exception as err:
        data = {'message': str(err)}
    return Response(data)


@api_view(['GET'])
def get_room_reservation(request, pk):
    try:
        room_reservation = RoomReservation.objects.get(pk=pk)
        ser = RoomReservationSerializer(room_reservation)
        return Response(ser.data)
    except Exception as err:
        data = {'message': str(err)}
    return Response(data)


@api_view(['GET'])
def delete_room_reservation(request, pk):
    try:
        room_reservation = RoomReservation.objects.get(pk=pk)
        room_reservation.delete()
        data = {'message', 'Service delete'}
    except Exception as err:
        data = {'message': str(err)}
    return Response(data)


""" END CRUD RoomReservation"""

"""START CRUD CarForRent"""


class CreateCarForRent(ListCreateAPIView):
    queryset = CarForRent.objects.all()
    serializer_class = CarForRentSerializer


class UpdateCarForRent(UpdateAPIView):
    queryset = RoomType.objects.all()
    serializer_class = RoomTypeSerializer


class DeleteCarForRent(DestroyAPIView):
    queryset = RoomType.objects.all()
    serializer_class = RoomTypeSerializer


""" END CRUD CarForRent"""

"""START CRUD CarRental"""


@api_view(['POST'])
def create_car_rental(request):
    try:
        ser = CarRentalSerializer(data=request.data)
        ser.is_valid(raise_exception=True)
        reservations = CarRental.objects.filter(
            car=ser.validated_data['car'],
            from_date__lt=ser.validated_data['to_date'],
            to_date__gt=ser.validated_data['from_date'],
        )

        if reservations.exists():
            data = {'status': 403, 'message': 'This car is already booked for the specified time period'}

        ser.save()
        data = ser.data
    except Exception as err:
        data = {'message': str(err)}
    return Response(data)


@api_view(['GET'])
def get_car_rental(request, pk):
    try:
        car = CarRental.objects.get(pk=pk)
        ser = CarRentalSerializer(car)
        return Response(ser.data)
    except Exception as err:
        data = {'message': str(err)}
    return Response(data)


@api_view(['GET'])
def delete_car_rental(request, pk):
    try:
        car = CarRental.objects.get(pk=pk)
        car.delete()
        data = {'message', 'service delete'}
    except Exception as err:
        data = {'message': str(err)}
    return Response(data)


""" END CRUD CarRental"""

""" START CRUD RestaurantAmenity"""


class CreateRestaurantAmenity(ListCreateAPIView):
    queryset = RestaurantAmenity.objects.all()
    serializer_class = RestaurantAmenitySerializer


class UpdateRestaurantAmenity(UpdateAPIView):
    queryset = RestaurantAmenity.objects.all()
    serializer_class = RestaurantAmenitySerializer


class GetAllRestaurantAmenity(UpdateAPIView):
    queryset = RestaurantAmenity.objects.all()
    serializer_class = RestaurantAmenitySerializer


class DeleteRestaurantAmenity(DestroyAPIView):
    queryset = RestaurantAmenity.objects.all()
    serializer_class = RestaurantAmenitySerializer


"""END CRUD RestaurantAmenity"""


"""START CRUD RESTAURANT """


class CreateRestaurant(ListCreateAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer

    def create(self, request, *args, **kwargs):
        try:
            user_id = request.data.get('user')
            user = User.objects.get(pk=user_id)
            if user.limit >= len(Restaurant.objects.filter(user=user)) and user.limit > 0:
                ser = self.get_serializer(data=request.data)
                ser.is_valid(raise_exception=True)
                restaurant = ser.save()
                images = request.data.getlist('images', [])
                amenities = self.request.data.getlist('amenities', [])
                for amenity in amenities:
                    restaurant.amenities.add(amenity)
                for i in images:
                    img = Images.objects.create(image=i)
                    restaurant.image.add(img)
                headers = self.get_success_headers(ser.data)
                data = ser.data
            else:
                data = {
                    'status': 403,
                    'message': 'The limit is set'
                }
        except Exception as err:
            data = {'message': str(err)}
        return Response(data)


class GetAllRestaurant(ListAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer


class EditRestaurant(UpdateAPIView):
    def edit(self, request, *args, **kwargs):
        try:
            ser = self.get_serializer(data=request.data)
            ser.is_valid(raise_exception=True)
            instance = self.get_object()
            instance.user = ser.validated_data.get('user')
            instance.name = ser.validated_data.get('name')
            instance.sub_category_location = ser.validated_data.get('sub_category_location')
            instance.lat = ser.validated_data.get('lat')
            instance.lot = ser.validated_data.get('lot')
            instance.location_text = ser.validated_data.get('location_text')
            instance.description = ser.validated_data.get('description')
            instance.number_tables = ser.validated_data.get('number_tables')
            instance.amenities.set(ser.validated_data.getlist('amenities', instance.amenities.all()))
            instance.delivery_service = ser.validated_data.get('delivery_service')
            instance.call_centre = ser.validated_data.get('call_centre')
            instance.restaurant_bank_shot = ser.validated_data.get('restaurant_bank_shot')
            instance.rating = ser.validated_data.get('rating')
            images = ser.validated_data.getlist('images', [])
            for i in images:
                img = Images.objects.create(image=i)
                instance.image.add(img)
            instance.save()
            ser = self.get_serializer(instance)
            data = ser.data
        except Exception as err:
            data = {'message': str(err)}
        return Response(data)


class DeleteRestaurant(ListAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer


"""END CRUD RESTAURANT """


""" START CRUD MealCategory"""


class CreateMealCategory(ListCreateAPIView):
    queryset = MealCategory.objects.all()
    serializer_class = MealCategorySerializer


class UpdateMealCategory(UpdateAPIView):
    queryset = MealCategory.objects.all()
    serializer_class = MealCategorySerializer


class GetAllMealCategory(UpdateAPIView):
    queryset = MealCategory.objects.all()
    serializer_class = MealCategorySerializer


class DeleteMealCategory(DestroyAPIView):
    queryset = MealCategory.objects.all()
    serializer_class = MealCategorySerializer


"""END CRUD MealCategory"""

""" START CRUD Meal"""


class CreateMeal(ListCreateAPIView):
    queryset = Meal.objects.all()
    serializer_class = MealSerializer


class UpdateMeal(UpdateAPIView):
    queryset = Meal.objects.all()
    serializer_class = MealSerializer


class GetAllMeal(UpdateAPIView):
    queryset = Meal.objects.all()
    serializer_class = MealSerializer


class DeleteMeal(DestroyAPIView):
    queryset = Meal.objects.all()
    serializer_class = MealSerializer


"""END CRUD Meal"""

""" START CRUD Table"""


class CreateTable(ListCreateAPIView):
    queryset = Table.objects.all()
    serializer_class = TableSerializer


class UpdateTable(UpdateAPIView):
    queryset = Table.objects.all()
    serializer_class = TableSerializer


class GetAllTable(UpdateAPIView):
    queryset = Table.objects.all()
    serializer_class = TableSerializer


class DeleteTable(DestroyAPIView):
    queryset = Table.objects.all()
    serializer_class = TableSerializer


"""END CRUD Table"""

""" START CRUD Order"""


class CreateOrder(ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class UpdateOrder(UpdateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class DeleteOrder(DestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


"""END CRUD Order"""

""" START CRUD Order"""


class CreateTableReservation(ListCreateAPIView):
    queryset = TableReservation.objects.all()
    serializer_class = TableReservationSerializer


class UpdateTableReservation(UpdateAPIView):
    queryset = TableReservation.objects.all()
    serializer_class = TableReservationSerializer


class DeleteTableReservation(DestroyAPIView):
    queryset = TableReservation.objects.all()
    serializer_class = TableReservationSerializer


"""END CRUD TableReservation"""

""" START CRUD Delivery"""


class CreateDelivery(ListCreateAPIView):
    queryset = Delivery.objects.all()
    serializer_class = DeliverySerializer


class DeleteDelivery(DestroyAPIView):
    queryset = Delivery.objects.all()
    serializer_class = DeliverySerializer


"""END CRUD TableReservation"""

""" START CRUD PaymentCheck"""


@api_view(['POST'])
def create_payment_check(request):
    try:
        user = request.POST.get('user')
        info = request.POST.get('info')
        summa = request.POST.get('summa')
        payment = PaymentCheck.objects.create(
            user=user,
            info=info,
            summa=summa,
        )
        Notification.objects.create(
            user=user,
            subject="To'lov",
            message=info,
        )
        ser = PaymentCheckSerializer(payment)
        data = ser.data
    except Exception as err:
        status = 500
        message = f"Request failed: {str(err)}"
        data = {
            'status': status,
            'message': message
        }
    return Response(data)


"""END CRUD PaymentCheck"""


"""START CRUD Contact"""


class CreateContact(ListCreateAPIView):
    queryset = PaymentCheck.objects.all()
    serializer_class = PaymentCheckSerializer


"""END CRUD Contact"""

"""START CRUD Notification"""


@api_view(['POST'])
def send_notification_by_user(request):
    try:
        user = request.POST.get('user')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        image = request.POST.get('image')
        notification = Notification.objects.create(
            user=user,
            subject=subject,
            message=message,
            image=image,
        )
        ser = NotificationSerializer(notification)
        data = ser.data
    except Exception as err:
        status = 500
        message = f"Request failed: {str(err)}"
        data = {
            'status': status,
            'message': message
        }
    return Response(data)


@api_view(['POST'])
def send_notification_by_users(request):
    try:
        users = User.objects.all()
        for i in users:
            user = i
            subject = request.POST.get('subject')
            message = request.POST.get('message')
            image = request.POST.get('image')
            notification = Notification.objects.create(
                user=user,
                subject=subject,
                message=message,
                image=image,
            )
        data = {'message': 'Message sent to users'}
    except Exception as err:
        status = 500
        message = f"Request failed: {str(err)}"
        data = {
            'status': status,
            'message': message
        }
    return Response(data)

"""END CRUD Notification"""

