from rest_framework.decorators import api_view
from rest_framework.response import Response
from dashboard.models import *
from dashboard.serializers import *


@api_view(['GET'])
def sub_category_location_by_category_location(request):
    try:
        category = request.GET['category_location']
        try:
            location = SubCategoryLocation.objects.filter(location_category_id=category)
            ser = SubCategoryLocationSerializer(location, many=True)
            data = ser.data
        except:
            status = 404
            message = "Request failed"
            data = {
                'status': status,
                'message': message,
            }
    except:
        status = 404
        message = "Sub location not found"
        data = {
            'status': status,
            'message': message,
        }
    return Response(data)


@api_view(['GET'])
def filter_search_by_hotel(request):
    try:
        sub_category_location = request.GET.get('sub_category')
        amenities = request.GET.getlist('amenities')
        try:
            hotel = Hotel.objects.filter(sub_category_location_id=sub_category_location, amenities__in=amenities)
            ser = HotelSerializer(hotel, many=True)
            data = ser.data
        except:
            status = 404
            message = "Request failed"
            data = {
                'status': status,
                'message': message,
            }
    except Exception as err:
        status = 404
        message = f"Bad Request: {str(err)}"
        data = {
            'status': status,
            'message': message,
        }
    return Response(data)


@api_view(['GET'])
def get_hotel(request, pk):
    try:
        hotel = Hotel.objects.get(pk=pk)
        ser = HotelSerializer(hotel)
        data = ser.data
    except Hotel.DoesNotExist:
        status = 404
        message = "Hotel not found"
        data = {
            'status': status,
            'message': message
        }
    except Exception as err:
        status = 500
        message = f"Request failed: {str(err)}"
        data = {
            'status': status,
            'message': message,
        }
    return Response(data)


@api_view(['GET'])
def room_type_by_hotel(request, pk):
    try:
        hotel = Hotel.objects.get(pk=pk)
        room_type = request.GET.getlist('room_type')
        try:
            room = Room.objects.filter(hotel=hotel, type__in=room_type)
            ser = RoomSerializer(room, many=True)
            data = ser.data
        except Room.DoesNotExist:
            status = 404
            message = "Hotel not found"
            data = {
                'status': status,
                'message': message
            }
    except Exception as err:
        status = 500
        message = f"Request failed: {str(err)}"
        data = {
            'status': status,
            'message': message
        }
    return Response(data)


@api_view(['GET'])
def rooms_by_hotel(request, pk):
    try:
        hotel = Hotel.objects.get(pk=pk)
        rooms = Room.objects.filter(hotel=hotel)
        ser = RoomSerializer(rooms, many=True)
        data = ser.data
    except Hotel.DoesNotExist:
        status = 404
        message = "Hotel not found"
        data = {
            'status': status,
            'message': message
        }
    except Exception as err:
        status = 500
        message = f"Request failed: {str(err)}"
        data = {
            'status': status,
            'message': message
        }
    return Response(data)


@api_view(['GET'])
def room_reservation_by_hotel(request, pk):
    try:
        hotel = Hotel.objects.get(pk=pk)
        if hotel.room_reservation:
            rooms = RoomReservation.objects.filter(hotel=hotel, reservation=False)
            ser = RoomReservationSerializer(rooms, many=True)
            data = ser.data
        else:
            data = {
                'status': 200,
                'message': 'The hotel does not have a reservation service'
            }
    except Hotel.DoesNotExist:
        status = 404
        message = "Hotel not found"
        data = {
            'status': status,
            'message': message
        }
    except Exception as err:
        status = 500
        message = f"Request failed: {str(err)}"
        data = {
            'status': status,
            'message': message
        }
    return Response(data)


@api_view(['GET'])
def car_for_rent_by_hotel(request, pk):
    try:
        hotel = Hotel.objects.get(pk=pk)
        cars = CarForRent.objects.filter(hotel=hotel, car_status=True)
        ser = CarForRentSerializer(cars, many=True)
        data = ser.data
    except Hotel.DoesNotExist:
        status = 404
        message = "Hotel not found"
        data = {
            'status': status,
            'message': message
        }
    except Exception as err:
        status = 500
        message = f"Request failed: {str(err)}"
        data = {
            'status': status,
            'message': message
        }
    return Response(data)


@api_view(['GET'])
def car_rental_by_hotel(request, pk):
    try:
        hotel = Hotel.objects.get(pk=pk)
        rentals = CarRental.objects.filter(hotel=hotel)
        ser = CarRentalSerializer(rentals, many=True)
        data = ser.data
    except Hotel.DoesNotExist:
        status = 404
        message = "Hotel not found"
        data = {
            'status': status,
            'message': message
        }
    except Exception as err:
        status = 500
        message = f"Request failed: {str(err)}"
        data = {
            'status': status,
            'message': message
        }
    return Response(data)


@api_view(['GET'])
def meal_by_restaurant(request, pk):
    try:
        restaurant = Restaurant.objects.get(pk=pk)
        meals = Meal.objects.filter(restaurant=restaurant)
        ser = MealSerializer(meals, many=True)
        data = ser.data
    except Restaurant.DoesNotExist:
        status = 404
        message = "Restaurant not found"
        data = {
            'status': status,
            'message': message
        }
    except Exception as err:
        status = 500
        message = f"Request failed: {str(err)}"
        data = {
            'status': status,
            'message': message
        }
    return Response(data)


@api_view(['GET'])
def table_by_restaurant(request, pk):
    try:
        restaurant = Restaurant.objects.get(pk=pk)
        tables = Table.objects.filter(restaurant=restaurant)
        ser = TableSerializer(tables, many=True)
        data = ser.data
    except Restaurant.DoesNotExist:
        status = 404
        message = "Restaurant not found"
        data = {
            'status': status,
            'message': message
        }
    except Exception as err:
        status = 500
        message = f"Request failed: {str(err)}"
        data = {
            'status': status,
            'message': message
        }
    return Response(data)


@api_view(['GET'])
def order_by_restaurant(request, pk):
    try:
        restaurant = Restaurant.objects.get(pk=pk)
        order = Order.objects.filter(restaurant=restaurant, status=False, is_payment=True)
        ser = OrderSerializer(order, many=True)
        data = ser.data
    except Restaurant.DoesNotExist:
        status = 404
        message = "Restaurant not found"
        data = {
            'status': status,
            'message': message
        }
    except Exception as err:
        status = 500
        message = f"Request failed: {str(err)}"
        data = {
            'status': status,
            'message': message
        }
    return Response(data)


@api_view(['GET'])
def table_reservation_by_restaurant(request, pk):
    try:
        restaurant = Restaurant.objects.get(pk=pk)
        tables = TableReservation.objects.filter(restaurant=restaurant, is_payment=True)
        ser = OrderSerializer(tables, many=True)
        data = ser.data
    except Restaurant.DoesNotExist:
        status = 404
        message = "Restaurant not found"
        data = {
            'status': status,
            'message': message
        }
    except Exception as err:
        status = 500
        message = f"Request failed: {str(err)}"
        data = {
            'status': status,
            'message': message
        }
    return Response(data)


@api_view(['GET'])
def delivery_by_restaurant(request, pk):
    try:
        restaurant = Restaurant.objects.get(pk=pk)
        delivery = Delivery.objects.filter(restaurant=restaurant, status=False, is_payment=True)
        ser = DeliverySerializer(delivery, many=True)
        data = ser.data
    except Restaurant.DoesNotExist:
        status = 404
        message = "Restaurant not found"
        data = {
            'status': status,
            'message': message
        }
    except Exception as err:
        status = 500
        message = f"Request failed: {str(err)}"
        data = {
            'status': status,
            'message': message
        }
    return Response(data)


@api_view(['GET'])
def user_payment_check(request, pk):
    try:
        user = User.objects.get(pk=pk)
        payments = PaymentCheck.objects.filter(user=user)
        ser = PaymentCheckSerializer(payments, many=True)
        data = ser.data
    except User.DoesNotExist:
        status = 404
        message = "User not found"
        data = {
            'status': status,
            'message': message
        }
    except Exception as err:
        status = 500
        message = f"Request failed: {str(err)}"
        data = {
            'status': status,
            'message': message
        }
    return Response(data)
