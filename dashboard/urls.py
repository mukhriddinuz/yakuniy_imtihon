from django.urls import path
from .views import *

urlpatterns =[
    path('create-check-identify/', CreateCheckIdentify.as_view()),
    path('delete-check-identify/<int:pk>/', DeleteCheckIdentify.as_view()),

    path('get-check-identify/<int:pk>/', get_check_identify),
    path('create-identification/', create_identification),

    path('create-category-location/', CreateCategoryLocation.as_view()),
    path('get-all-category-location/', GetCategoryLocation.as_view()),
    path('update-category-location/<int:pk>/', UpdateCategoryLocation.as_view()),
    path('delete-category-location/<int:pk>/', DeleteCategoryLocation.as_view()),

    path('create-sub-category-location/', CreateSubCategoryLocation.as_view()),
    path('get-all-sub-category-location/', GetSubCategoryLocation.as_view()),
    path('update-sub-category-location/<int:pk>/', UpdateSubCategoryLocation.as_view()),
    path('delete-sub-category-location/<int:pk>/', DeleteSubCategoryLocation.as_view()),

    path('create-hotel-amenity/', CreateHotelAmenity.as_view()),
    path('get-all-hotel-amenity/', GetHotelAmenity.as_view()),
    path('update-hotel-amenity/<int:pk>/', UpdateHotelAmenity.as_view()),
    path('delete-hotel-amenity/<int:pk>/', DeleteHotelAmenity.as_view()),

    path('create-hotel/', CreateHotel.as_view()),
    path('update-hotel/<int:pk>/', EditHotel.as_view()),
    path('get-all-hotel/', GetAllHotel.as_view()),
    path('delete-hotel/<int:pk>/', DeleteHotel.as_view()),

    path('create-room-type/', CreateRoomType.as_view()),
    path('get-all-room-type/', GetAllRoomType.as_view()),
    path('update-room-type/<int:pk>/', UpdateRoomType.as_view()),
    path('delete-room-type/<int:pk>/', DeleteRoomType.as_view()),

    path('create-room-reservation/', create_room_reservation),
    path('get-room-reservation/<int:pk>/', get_room_reservation),
    path('delete-room-reservation/<int:pk>/', delete_room_reservation),

    path('create-car-rental/', create_car_rental),
    path('get-room-reservation/<int:pk>/', get_car_rental),
    path('delete-room-reservation/<int:pk>/', delete_room_reservation),

    path('create-restaurant-amenity/', CreateRestaurantAmenity.as_view()),
    path('get-all-restaurant-amenity/', GetAllRestaurantAmenity.as_view()),
    path('update-restaurant-amenity/<int:pk>/', UpdateRestaurantAmenity.as_view()),
    path('delete-restaurant-amenity/<int:pk>/', DeleteRestaurantAmenity.as_view()),

    path('create-restaurant/', CreateRestaurant.as_view()),
    path('update-restaurant/<int:pk>/', EditRestaurant.as_view()),
    path('get-all-restaurant/', GetAllRestaurant.as_view()),
    path('delete-restaurant/<int:pk>/', DeleteRestaurant.as_view()),

    path('create-meal-category/', CreateMealCategory.as_view()),
    path('update-meal-category/<int:pk>/', UpdateMealCategory.as_view()),
    path('get-all-meal-category/', GetAllMealCategory.as_view()),
    path('delete-meal-category/<int:pk>/', DeleteMealCategory.as_view()),

    path('create-meal/', CreateMeal.as_view()),
    path('update-meal/<int:pk>/', UpdateMeal.as_view()),
    path('get-all-meal/', GetAllMeal.as_view()),
    path('delete-meal/<int:pk>/', DeleteMeal.as_view()),

    path('create-table/', CreateTable.as_view()),
    path('update-table/<int:pk>/', UpdateTable.as_view()),
    path('get-all-table/', GetAllTable.as_view()),
    path('delete-table/<int:pk>/', DeleteTable.as_view()),

    path('create-order/', CreateOrder.as_view()),
    path('update-order/<int:pk>/', UpdateOrder.as_view()),
    path('delete-order/<int:pk>/', DeleteOrder.as_view()),

    path('create-table-reservation/', CreateTableReservation.as_view()),
    path('update-table-reservation/<int:pk>/', UpdateTableReservation.as_view()),
    path('delete-table-reservation/<int:pk>/', DeleteTableReservation.as_view()),

    path('create-delivery/', CreateDelivery.as_view()),
    path('delete-table-reservation/<int:pk>/', DeleteDelivery.as_view()),

    path('create-payment-check/', create_payment_check),
    path('create-contact/', CreateContact.as_view()),
    path('send-notification-by-user', send_notification_by_user),
    path('send-notification-by-users', send_notification_by_users),
]
