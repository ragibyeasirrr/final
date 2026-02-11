from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator
from user.models import User
from uuid import uuid4
from cloudinary.models import CloudinaryField

# Create your models here.
class hotelCategory(models.Model):
    name=models.CharField(max_length=50)
    description=models.TextField(blank=True,null=True)

    def __str__(self):
        return self.name

class Hotel(models.Model):
    name=models.CharField( max_length=100)
    address=models.CharField(max_length=200)
    description=models.TextField(blank=True,null=True)
    #image=models.ImageField(upload_to='hote/',blank=True,null=True)
    image = CloudinaryField('image', blank=True, null=True)
    category=models.ForeignKey(hotelCategory,on_delete=models.CASCADE,related_name='hotel')
    # owner=models.ForeignKey(User,on_delete=models.CASCADE,related_name='hotel')

    def __str__(self):
        return self.name

class Facility(models.Model):
    name=models.CharField(max_length=100)
    description=models.TextField(blank=True,null=True)

    def __str__(self):
        return self.name


class room(models.Model):
    hotel=models.ForeignKey(Hotel,on_delete=models.CASCADE,related_name='room')
    room_num=models.CharField(max_length=50,unique=True)
    cost_per_day=models.DecimalField(max_digits=10,decimal_places=2)
    capecity=models.PositiveIntegerField( validators=[MinValueValidator(1), MaxValueValidator(5)])
    facility=models.ManyToManyField(Facility, related_name='room')
    available=models.BooleanField(default=True)

    def __str__(self):
        return f"{self.hotel.name} - Room {self.room_num}"
    



class Review(models.Model):
    hotel= models.ForeignKey(Hotel, on_delete=models.CASCADE,related_name='review')
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    ratings = models.PositiveIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(10)])
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Review by {self.user.first_name} on {self.hotel.name}" 

class roomImg(models.Model):
    rooms=models.ForeignKey(room,on_delete=models.CASCADE,related_name='images')
    #image = models.ImageField(upload_to="images/",blank=True,null=True) # validators=[validate_file_size]
    image = CloudinaryField('image', blank=True, null=True) 

class Cart_Booking(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="cart")
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"Booking cart of {self.user.first_name}"

class Cart_bookingRoom(models.Model):
    cartbooking=models.ForeignKey(
        Cart_Booking, on_delete=models.CASCADE, related_name="CartBookingRoom")
    cartRoom= models.ForeignKey(room,on_delete=models.CASCADE,related_name='cart_room') 

    class Meta:
        unique_together = [['cartbooking', 'cartRoom']]

    def __str__(self):
        return f"{self.cartRoom.hotel.name}"    


class Booking(models.Model):
    NOT_PAID='not paid'
    PENDING='pending'
    BOOKED='booked'
    CANCEL='cancel'
    STATUS_CHOICE=[
        (NOT_PAID,'not paid'),
        (PENDING,'pending'),
        (BOOKED,'booked'),
        (CANCEL,'cancel')]
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="orders")
    status = models.CharField(
        max_length=20, choices=STATUS_CHOICE, default=NOT_PAID)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class bookingRoom(models.Model):
    booking=models.ForeignKey(Booking,on_delete=models.CASCADE,related_name='rooms')
    Room= models.ForeignKey(room,on_delete=models.CASCADE,related_name='booking_room') 
    cost_per_day=models.DecimalField(max_digits=10,decimal_places=2)









