from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid


class CheckIdentify(models.Model):
    user = models.ForeignKey(to='User', on_delete=models.CASCADE)
    video = models.FileField(upload_to='iden_video/')
    passport_image = models.ImageField(upload_to='passport_images/')
    STATUS = (
        (1, 'Canceled'),
        (2, 'Confirmed'),
        (3, 'Is expected'),
    )
    status = models.IntegerField(choices=STATUS, default=3)


class Identification(models.Model):
    user = models.ForeignKey(to="User", on_delete=models.CASCADE, null=True, blank=True)
    check_identify = models.ForeignKey(to='CheckIdentify', on_delete=models.CASCADE)
    country_code = models.CharField(max_length=3)
    passport_number = models.CharField(max_length=20)
    date_of_birth = models.DateField()
    nationality = models.CharField(max_length=255)
    place_of_birth = models.CharField(max_length=255)
    SEX_CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female')
    )
    sex = models.CharField(max_length=6, choices=SEX_CHOICES)
    passport_authority = models.CharField(max_length=255)


class User(AbstractUser):
    id = models.BigIntegerField(editable=False, primary_key=True)
    clone_password = models.CharField(max_length=255, null=True, blank=True)
    avatar = models.ImageField(upload_to='user_avatar_photo/', null=True, blank=True)
    STATUS_CHOICES = (
        ("SuperUser", "SuperUser"),
        ('Director', 'Director'),
        ("Member", "Member"),
    )
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Member')
    phone_number = models.CharField(max_length=13, unique=True, null=True, blank=True,)
    limit = models.IntegerField(default=0)
    approved = models.BooleanField(default=False)

    class Meta(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def save(self, *args, **kwargs):
        if not self.id:
            self.id = int('9' + str(uuid.uuid4().int)[1:11])
        super(User, self).save(*args, **kwargs)


class CategoryLocation(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class SubCategoryLocation(models.Model):
    location_category = models.ForeignKey(to='CategoryLocation', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Images(models.Model):
    image = models.ImageField(upload_to='images/')


class HotelAmenity(models.Model):
    name = models.CharField(max_length=255)
    create_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Hotel(models.Model):
    user = models.ForeignKey(to='User', on_delete=models.PROTECT)
    name = models.CharField(max_length=255)
    hotel_bank_number = models.PositiveIntegerField(null=True, blank=True)
    sub_category_location = models.ForeignKey(to='SubCategoryLocation', on_delete=models.PROTECT)
    lat = models.CharField(max_length=255)
    lot = models.CharField(max_length=255)
    location_text = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    call_centre = models.CharField(max_length=25)
    number_rooms = models.IntegerField()
    amenities = models.ManyToManyField(to='HotelAmenity', blank=True)
    car_rental = models.BooleanField(default=False)
    room_reservation = models.BooleanField(default=False)
    restaurant_and_cafe = models.BooleanField(default=False)
    shopping = models.BooleanField(default=False)
    cleaning_room_service = models.BooleanField(default=False)
    rating = models.FloatField(default=0)
    image = models.ManyToManyField(to='Images', blank=True)

    def __str__(self):
        return self.name


class RoomType(models.Model):
    name = models.CharField(max_length=255)
    info = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class RoomImages(models.Model):
    img = models.ImageField(upload_to='room_images/')


class Room(models.Model):
    hotel = models.ForeignKey(to='Hotel', on_delete=models.CASCADE)
    type = models.ForeignKey(to='RoomType', on_delete=models.PROTECT)
    room_image = models.ManyToManyField(to='RoomImages')
    room_number = models.IntegerField()
    kitchen = models.BooleanField(default=True)
    bathroom = models.BooleanField(default=True)
    free_wifi = models.BooleanField(default=True)
    free_parking = models.BooleanField(default=False)
    number_people = models.IntegerField()
    price_for_day = models.IntegerField()
    reservation = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.room_number} room'


class RoomReservation(models.Model):
    user = models.ForeignKey(to='User', on_delete=models.CASCADE)
    hotel = models.ForeignKey(to='Hotel', on_delete=models.CASCADE)
    room = models.ForeignKey(to='Room', on_delete=models.CASCADE)
    from_date = models.DateTimeField()
    to_date = models.DateTimeField()

    def __str__(self):
        return f'{self.user.username} - {self.hotel.name}'


class CarForRent(models.Model):
    hotel = models.ForeignKey(to='Hotel', on_delete=models.CASCADE)
    car_name = models.CharField(max_length=255)
    car_brand = models.CharField(max_length=255)
    car_number = models.CharField(max_length=255)
    FUEL = (
        ("Electr", "Electr"),
        ('Gas', 'Gas'),
        ('Benzine', 'Benzine'),
        ('Gas and Benzine', 'Gas and Benzine')
    )
    car_fuel = models.CharField(max_length=50, choices=FUEL, default='Benzine')
    car_status = models.BooleanField(default=True)
    price_for_day = models.IntegerField()

    def __str__(self):
        return self.car_name


class CarRental(models.Model):
    hotel = models.ForeignKey(to='Hotel', on_delete=models.CASCADE)
    user = models.ForeignKey(to='User', on_delete=models.CASCADE)
    car = models.ForeignKey(to='CarForRent', on_delete=models.CASCADE)
    from_date = models.DateField()
    to_date = models.DateField()


# End hotel models


class RestaurantAmenity(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Restaurant(models.Model):
    user = models.ForeignKey(to='User', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    sub_category_location = models.ForeignKey(to='SubCategoryLocation', on_delete=models.CASCADE)
    lat = models.CharField(max_length=255)
    lot = models.CharField(max_length=255)
    location_text = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    number_tables = models.IntegerField()
    amenities = models.ManyToManyField(to='RestaurantAmenity')
    delivery_service = models.BooleanField(default=False)
    call_centre = models.CharField(max_length=20)
    image = models.ManyToManyField(to='Images')
    restaurant_bank_shot = models.PositiveIntegerField(null=True, blank=True)
    rating = models.FloatField(default=0)

    def save(self, *args, **kwargs):
        self.code = self.user.username
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class MealCategory(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Meal(models.Model):
    restaurant = models.ForeignKey(to="Restaurant", on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    category = models.ForeignKey(to="MealCategory", on_delete=models.PROTECT)
    description = models.TextField()
    price = models.FloatField()

    def __str__(self):
        return self.name


class Table(models.Model):
    restaurant = models.ForeignKey(to='Restaurant', on_delete=models.CASCADE)
    number_people = models.IntegerField()
    number = models.IntegerField()
    code = models.CharField(max_length=255)

    def __str__(self):
        return self.code


class Order(models.Model):
    user = models.ForeignKey(to='User', on_delete=models.CASCADE)
    restaurant = models.ForeignKey(to='Restaurant', on_delete=models.CASCADE)
    meals = models.ManyToManyField(to='Meal')
    table = models.ForeignKey(to='Table', on_delete=models.CASCADE)
    status = models.BooleanField(default=False)
    is_payment = models.BooleanField(default=False)


class TableReservation(models.Model):
    user = models.ForeignKey(to='User', on_delete=models.CASCADE)
    restaurant = models.ForeignKey(to='Restaurant', on_delete=models.CASCADE)
    meals = models.ManyToManyField(to='Meal', blank=True)
    from_date = models.DateTimeField()
    status = models.BooleanField(default=False)
    is_payment = models.BooleanField(default=False)


class Delivery(models.Model):
    user = models.ForeignKey(to='User', on_delete=models.CASCADE)
    restaurant = models.ForeignKey(to='Restaurant', on_delete=models.CASCADE)
    meals = models.ManyToManyField(to='Meal')
    location = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    status = models.BooleanField(default=False)
    is_payment = models.BooleanField(default=False)


# End restaurant models


class PaymentCheck(models.Model):
    user = models.ForeignKey(to='User', on_delete=models.CASCADE)
    info = models.TextField()
    summa = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now=True)


class Contact(models.Model):
    user = models.ForeignKey(to='User', on_delete=models.CASCADE)
    subject = models.CharField(max_length=255)
    message = models.TextField()
    image = models.ImageField(upload_to='contact_image/', null=True, blank=True)


class Notification(models.Model):
    user = models.ForeignKey(to='User', on_delete=models.CASCADE)
    subject = models.CharField(max_length=255)
    message = models.TextField()
    image = models.ImageField(upload_to='Notification_image/', null=True, blank=True)
