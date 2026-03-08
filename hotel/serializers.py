from rest_framework import serializers
from decimal import Decimal
from hotel.models import Hotel,hotelCategory,room,Facility,roomImg,Booking,bookingRoom,Review,RoomReview,Cart_Booking,Cart_bookingRoom
from django.contrib.auth import get_user_model
from hotel.services import BookingService

# hotel

class hotel_cat(serializers.ModelSerializer):
    class Meta:
        model =hotelCategory
        fields = ['id', 'name','description']  

class hotelserializerr(serializers.ModelSerializer):
    image = serializers.ImageField(required=False)
    
    class Meta:
        model=Hotel
        fields=['id','name','address','description','image','category']


class hotelserializer(serializers.ModelSerializer):
    image = serializers.ImageField(required=False)
    category=hotel_cat(read_only=True)
    class Meta:
        model=Hotel
        fields=['id','name','address','description','image','category']

class roomImageSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(required=False)
    class Meta:
        model = roomImg
        fields = ['id','image']        


class room_fac(serializers.ModelSerializer):
    class Meta:
        model =Facility
        fields = ['id', 'name','description']     


class room_seria(serializers.ModelSerializer):
    
    class Meta:
        model = room
        fields = ['id', 'hotel','room_num','cost_per_day','capecity','facility','description','available']             

class room_ser(serializers.ModelSerializer):
    facility=room_fac(many=True)
    hotel=hotelserializerr()
    images=roomImageSerializer(many=True, read_only=True)
    class Meta:
        model = room
        fields = ['id', 'hotel','room_num','cost_per_day','capecity','facility','description','images','available']  
class SimpleUserSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField(
        method_name='get_current_user_name')

    class Meta:
        model = get_user_model()
        fields = ['id', 'name']

    def get_current_user_name(self, obj):
        return obj.get_full_name()

class ReviewSerializer(serializers.ModelSerializer):
   
    user = serializers.SerializerMethodField(method_name='get_user')

    class Meta:
        model = Review
        fields = ['id', 'user', 'hotel', 'ratings', 'comment']
        read_only_fields = ['user', 'hotel']

    def get_user(self, obj):
        return SimpleUserSerializer(obj.user).data

    def create(self, validated_data):
        hotel_id = self.context['hotel_id']
        return Review.objects.create(hotel_id=hotel_id, **validated_data)

class reviewSerializer(serializers.ModelSerializer):
   
    user = serializers.SerializerMethodField(method_name='get_user')

    class Meta:
        model = RoomReview
        fields = ['id', 'user', 'rooms', 'ratings', 'comment']
        read_only_fields = ['user', 'rooms']

    def get_user(self, obj):
        return SimpleUserSerializer(obj.user).data

    def create(self, validated_data):
        rooms_id = self.context['rooms_id']
        return RoomReview.objects.create(rooms_id=rooms_id, **validated_data)



class bookingroomSerializer(serializers.ModelSerializer):
    cartRoom = room_seria()
    cost_of_room = serializers.SerializerMethodField(
        method_name='get_total_price')

    class Meta:
        model = Cart_bookingRoom
        fields = ['id', 'cartRoom', 'cost_of_room']

    def get_total_price(self, cart_bookingroom: Cart_bookingRoom):
        return cart_bookingroom.cartRoom.cost_per_day





class CartBookingSerializer(serializers.ModelSerializer):
    CartBookingRoom= bookingroomSerializer(many=True, read_only=True)
    total_price = serializers.SerializerMethodField(
        method_name='get_total_price')
    user = serializers.SerializerMethodField(method_name='get_user')
    class Meta:
        model = Cart_Booking
        fields = ['id', 'user', 'CartBookingRoom', 'total_price']
        read_only_fields = ['user']
    def get_user(self, obj):
        return SimpleUserSerializer(obj.user).data
    def get_total_price(self, cart_booking: Cart_Booking):
        return sum(
            [item.cartRoom.cost_per_day for item in cart_booking.CartBookingRoom.all()])
    
    def validate_user(self, user): 
        if Cart_Booking.objects.filter(user=user).exists():
                raise serializers.ValidationError(
                "You already have a cart"
            )
        return user

# class CartBookingSerializer(serializers.ModelSerializer):
#     CartBookingRoom = bookingroomSerializer(many=True, read_only=True)

#     total_price = serializers.SerializerMethodField()
#     user = serializers.SerializerMethodField()

#     class Meta:
#         model = Cart_Booking
#         fields = ['id', 'user', 'CartBookingRoom', 'total_price']

#     def get_user(self, obj):
#         return SimpleUserSerializer(obj.user).data

#     def get_total_price(self, cart_booking):
#         return sum(
#             item.cartRoom.cost_per_day
#             for item in cart_booking.CartBookingRoom.all()
#         )    
class AddbookingroomSerializer(serializers.ModelSerializer):
    cartRoom_id = serializers.IntegerField()

    class Meta:
        model = Cart_bookingRoom
        fields = ['id', 'cartRoom_id']

    def save(self, **kwargs):
        cartbooking_id = self.context['cartbooking_id']
        cartRoom_id = self.validated_data['cartRoom_id']
        

        try:
            cart_bookingroom = Cart_bookingRoom.objects.get(
                cartbooking_id=cartbooking_id, cartRoom_id=cartRoom_id)
            
            self.instance = cart_bookingroom
        except  Cart_bookingRoom.DoesNotExist:
            cart_bookingroom = Cart_bookingRoom.objects.create(
                cartbooking_id=cartbooking_id, cartRoom_id=cartRoom_id)
            self.instance = cart_bookingroom

        return self.instance
    def validate_cartRoom_id(self, value):
        if not room.objects.filter(pk=value).exists():
            raise serializers.ValidationError(
                f"Room with id {value} does not exists")
        return value


class mostBookedroomSer(serializers.ModelSerializer):
    total = serializers.IntegerField(read_only=True)

    class Meta:
        model = room
        fields = ['id', 'room_num', 'total']


class topfiveuser(serializers.Serializer):
    user = serializers.IntegerField()  
    total_bookings = serializers.IntegerField()

# class Addbookingroom_ser(serializers.ModelSerializer):
#     class Meta:
#         model = bookingRoom
#         fields = ['Room']

#     def create(self, validated_data):
#         booking_id = self.context['booking_id']
#         Room = validated_data['Room']

#         return bookingRoom.objects.create(
#             booking_id=booking_id,
#             Room=Room,
#             cost_per_day=Room.cost_per_day
#         )   

class EmptySerializer(serializers.Serializer):
    pass


class CreateBookingser(serializers.Serializer):
    

    cartbooking_id= serializers.UUIDField()

    def validate_cartbooking_id(self,cartbooking_id):
        if not Cart_Booking.objects.filter(pk=cartbooking_id).exists():
            raise serializers.ValidationError('No cart found with this id')

        if not Cart_bookingRoom.objects.filter(cartbooking_id=cartbooking_id).exists():
            raise serializers.ValidationError('Cart is empty')

        return cartbooking_id
    def create(self, validated_data):
        user_id = self.context['user_id']
        cartbooking_id=validated_data['cartbooking_id']

        

        try:
            booking = BookingService.create_booking(user_id=user_id, cartbooking_id= cartbooking_id)
            return booking
        except ValueError as e:
            raise serializers.ValidationError(str(e))

    def to_representation(self, instance):
        return bookingSer(instance).data
class bookingroom_ser(serializers.ModelSerializer):
    Room = room_ser(read_only=True)  
    class Meta:
        model = bookingRoom
        fields = ['id', 'Room', 'cost_per_day']
        read_only_fields = fields    

class UpdatebookingSer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ['status']


class bookingSer(serializers.ModelSerializer):
    rooms = bookingroom_ser(many=True)
    user = serializers.SerializerMethodField(method_name='get_user')
    def get_user(self, obj):
        return SimpleUserSerializer(obj.user).data

    class Meta:
        model = Booking
        fields = ['id', 'user', 'status', 'total_price', 'created_at', 'rooms']        
