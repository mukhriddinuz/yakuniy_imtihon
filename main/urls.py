from django.urls import path
from .views import *
urlpatterns = [
    path('get-sub-category-by.category/', sub_category_location_by_category_location),
    path('filter-search-by-hotel/', filter_search_by_hotel),
    path('get-hotel/<int:pk>/', get_hotel),
    path('room-type-by-hotel/<int:pk>/', room_type_by_hotel),
    path('rooms-by-hotel/<int:pk>/', rooms_by_hotel),
    path('rooms-reservation-by-hotel/<int:pk>/', room_reservation_by_hotel),
    path('car-for-rent-by-hotel/<int:pk>/', car_for_rent_by_hotel),

    path('meal-by-restaurant/<int:pk>/', meal_by_restaurant),
    path('table-by-restaurant/<int:pk>/', table_by_restaurant),
    path('order-by-restaurant/<int:pk>/', order_by_restaurant),
    path('table-reservation-by-restaurant/<int:pk>/', table_reservation_by_restaurant),
    path('delivery-by-restaurant/<int:pk>/', table_reservation_by_restaurant),

    path('user-payments/<int:pk>/', user_payment_check),
]
