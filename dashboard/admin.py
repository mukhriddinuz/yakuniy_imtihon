from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext, gettext_lazy as _
from .models import *


@admin.register(User)
class EmployeeAdmin(UserAdmin):
    list_display = ['id', 'username', 'first_name', 'status', 'is_active']
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'email')}),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        (_('Extra'), {'fields': ('clone_password', 'avatar', 'status', 'phone_number', 'limit', 'approved')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )


admin.site.register(Identification)
admin.site.register(CategoryLocation)
admin.site.register(SubCategoryLocation)
admin.site.register(Images)
admin.site.register(HotelAmenity)
admin.site.register(Hotel)
admin.site.register(RoomType)
admin.site.register(RoomImages)
admin.site.register(Room)
admin.site.register(RoomReservation)
admin.site.register(CarForRent)
admin.site.register(CarRental)
admin.site.register(RestaurantAmenity)
admin.site.register(Restaurant)
admin.site.register(MealCategory)
admin.site.register(Meal)
admin.site.register(Table)
admin.site.register(Order)
admin.site.register(TableReservation)
admin.site.register(Delivery)
admin.site.register(PaymentCheck)
admin.site.register(CheckIdentify)
