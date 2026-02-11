from django.db import transaction
from rest_framework.exceptions import PermissionDenied, ValidationError
from hotel.models import Booking, bookingRoom,Cart_Booking,Cart_bookingRoom


class BookingService:
    @staticmethod
    def create_booking(user_id,cartbooking_id):
        with transaction.atomic():
            cartbooking=Cart_Booking.objects.get(pk=cartbooking_id)
            # bookings=booking.rooms.select_related('Room').all()
            
            cartbookings = cartbooking.CartBookingRoom.select_related('cartRoom').all()
            total_price=sum([ room.cartRoom.cost_per_day for room in cartbookings])
            booking = Booking.objects.create(
                user_id=user_id,
                total_price=total_price,
                status = Booking.PENDING
            )
            booking_room=[bookingRoom(booking=booking,Room=room.cartRoom,cost_per_day=room.cartRoom.cost_per_day)for room in cartbookings]
            bookingRoom.objects.bulk_create(booking_room)
            cartbooking.delete()
            return booking
    @staticmethod
    def cancel_booking(booking, user):
        if user.is_staff:
            booking.status = Booking.CANCEL
            booking.save()
            return booking
        if booking.user != user:
            raise PermissionDenied(
                {"detail": "You can only cancel your own booking"})   
        if booking.status == Booking.BOOKED:
            raise ValidationError({"detail": "You can not cancel an Booked booking"})
        booking.status = Booking.CANCEL
        booking.save()
        return booking

