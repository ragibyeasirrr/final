from django.shortcuts import render
from hotel.models import Hotel,hotelCategory,room,Facility,roomImg,Booking,bookingRoom,Review,Cart_Booking,Cart_bookingRoom
from hotel.services import BookingService
from rest_framework.viewsets import ModelViewSet
from hotel.serializers import hotelserializer,hotel_cat,room_seria,room_fac,roomImageSerializer,ReviewSerializer,bookingroom_ser,CartBookingSerializer,EmptySerializer,UpdatebookingSer,bookingSer,CreateBookingser,AddbookingroomSerializer,bookingroomSerializer,mostBookedroomSer,topfiveuser,room_ser,hotelserializerr
# Create your views here.
from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin, DestroyModelMixin
from rest_framework.viewsets import GenericViewSet, ModelViewSet
from rest_framework.decorators import action
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from hotel import serializers as bookingSz
from django.utils.timezone import now
from datetime import timedelta
from django.db.models import Count, Sum
from rest_framework.views import APIView
from drf_yasg.utils import swagger_auto_schema
from hotel.permissions import IsAdminOrReadOnly,IsReviewAuthorOrReadonly

class hotelviewset(ModelViewSet):
    queryset=Hotel.objects.all()
    serializer_class=hotelserializer
    def get_serializer_class(self):
        if self.request.method == 'POST':
            return hotelserializerr
        return  hotelserializer
    permission_classes = [IsAdminOrReadOnly]
    @swagger_auto_schema(
        operation_summary='Retrive all hotel'
    )
    def list(self, request, *args, **kwargs):
        """Retrive all the hotel"""
        return super().list(request, *args, **kwargs)
    
    @swagger_auto_schema(
        operation_summary='create a list of hotel'
    )
    def create(self, request, *args, **kwargs):
        """Only authenticated admin can create hotel"""
        return super().create(request, *args, **kwargs)
    @swagger_auto_schema(
        operation_summary='Retrive  a single hotel'
    )
    def retrieve(self, request, *args, **kwargs):
        """Retrive  a single hotel """
        return super().retrieve(request, *args, **kwargs)
    @swagger_auto_schema(
        operation_summary='Update  a single hotel'
    )
    def update(self, request, *args, **kwargs):
        """ Update  a single hotel """
        return super().update(request, *args, **kwargs)
    @swagger_auto_schema(
        operation_summary='Delete  a single hotel'
    )
    def destroy(self, request, *args, **kwargs):
        """ Delete  a single hotel """
        return super().destroy(request, *args, **kwargs)
    @swagger_auto_schema(
        operation_summary='patch  a single hotel'
    )
    def partial_update(self, request, *args, **kwargs):
        """ patch a single hotel"""
        return super().partial_update(request, *args, **kwargs)

class hotel_cat_viewset(ModelViewSet):
    queryset=hotelCategory.objects.all()
    serializer_class=hotel_cat
    
    permission_classes = [IsAdminOrReadOnly]
    @swagger_auto_schema(
        operation_summary='Retrive all Hotel catrgory'
    )
    def list(self, request, *args, **kwargs):
        """Retrive all the Hotel catrgory"""
        return super().list(request, *args, **kwargs)
    
    @swagger_auto_schema(
        operation_summary='create a list of Hotel catrgory'
    )
    def create(self, request, *args, **kwargs):
        """Only authenticated user can create Hotel catrgory"""
        return super().create(request, *args, **kwargs)
    @swagger_auto_schema(
        operation_summary='Retrive  a single Hotel catrgory'
    )
    def retrieve(self, request, *args, **kwargs):
        """Retrive  a single Hotel catrgory """
        return super().retrieve(request, *args, **kwargs)
    @swagger_auto_schema(
        operation_summary='Update  a single Hotel catrgory'
    )
    def update(self, request, *args, **kwargs):
        """ Update  a single Hotel catrgory """
        return super().update(request, *args, **kwargs)
    @swagger_auto_schema(
        operation_summary='Delete  a single Hotel catrgory'
    )
    def destroy(self, request, *args, **kwargs):
        """ Delete  a single Hotel catrgory """
        return super().destroy(request, *args, **kwargs)
    @swagger_auto_schema(
        operation_summary='patch  a single Hotel catrgory'
    )
    def partial_update(self, request, *args, **kwargs):
        """ patch a single Hotel catrgory"""
        return super().partial_update(request, *args, **kwargs)


class room_viewset(ModelViewSet):
    queryset=room.objects.all()
    serializer_class=room_seria 
    permission_classes = [IsAdminOrReadOnly]  
    def get_serializer_class(self):
        if self.request.method == 'POST':
            return room_seria 
        return  room_ser 
    @swagger_auto_schema(
        operation_summary='Retrive all Room'
    )
    def list(self, request, *args, **kwargs):
        """Retrive all the Room"""
        return super().list(request, *args, **kwargs)
    
    @swagger_auto_schema(
        operation_summary='create a list of Room'
    )
    def create(self, request, *args, **kwargs):
        """Only authenticated admin can create Room"""
        return super().create(request, *args, **kwargs)
    @swagger_auto_schema(
        operation_summary='Retrive  a single Room'
    )
    def retrieve(self, request, *args, **kwargs):
        """Retrive  a single Room """
        return super().retrieve(request, *args, **kwargs)
    @swagger_auto_schema(
        operation_summary='Update  a single Room'
    )
    def update(self, request, *args, **kwargs):
        """ Update  a single Room """
        return super().update(request, *args, **kwargs)
    @swagger_auto_schema(
        operation_summary='Delete  a single Room'
    )
    def destroy(self, request, *args, **kwargs):
        """ Delete  a single Room """
        return super().destroy(request, *args, **kwargs)
    @swagger_auto_schema(
        operation_summary='patch  a single Rooml'
    )
    def partial_update(self, request, *args, **kwargs):
        """ patch a single Room"""
        return super().partial_update(request, *args, **kwargs)


class room_fac_viewset(ModelViewSet):
    queryset=Facility.objects.all()
    serializer_class=room_fac 
    
    permission_classes = [IsAdminOrReadOnly] 

    @swagger_auto_schema(
        operation_summary='Retrive all Room Facility'
    )
    def list(self, request, *args, **kwargs):
        """Retrive all the Room Facility"""
        return super().list(request, *args, **kwargs)
    
    @swagger_auto_schema(
        operation_summary='create a list of Room Facility'
    )
    def create(self, request, *args, **kwargs):
        """Only authenticated admin can create Room Facility"""
        return super().create(request, *args, **kwargs)
    @swagger_auto_schema(
        operation_summary='Retrive  a single Room Facility'
    )
    def retrieve(self, request, *args, **kwargs):
        """Retrive  a single Room Facility """
        return super().retrieve(request, *args, **kwargs)
    @swagger_auto_schema(
        operation_summary='Update  a single Room Facility'
    )
    def update(self, request, *args, **kwargs):
        """ Update  a single Room Facility """
        return super().update(request, *args, **kwargs)
    @swagger_auto_schema(
        operation_summary='Delete  a single Room Facility'
    )
    def destroy(self, request, *args, **kwargs):
        """ Delete  a single Room Facility """
        return super().destroy(request, *args, **kwargs)
    @swagger_auto_schema(
        operation_summary='patch  a single Room Facility'
    )
    def partial_update(self, request, *args, **kwargs):
        """ patch a single Room Facility"""
        return super().partial_update(request, *args, **kwargs)


class room_img_viewset(ModelViewSet):
    parser_classes = [MultiPartParser, FormParser]
    queryset=roomImg.objects.all()
    serializer_class=roomImageSerializer 
    permission_classes = [IsAdminOrReadOnly]
    def perform_create(self, serializer):
        serializer.save(rooms_id=self.kwargs.get('rooms_pk'))
    @swagger_auto_schema(
        operation_summary='Retrive all Room Image'
    )
    def list(self, request, *args, **kwargs):
        """Retrive all the Room Image"""
        return super().list(request, *args, **kwargs)
    
    @swagger_auto_schema(
        operation_summary='create a list of Room Image'
    )
    def create(self, request, *args, **kwargs):
        """Only authenticated admin can create Room Image"""
        return super().create(request, *args, **kwargs)
    @swagger_auto_schema(
        operation_summary='Retrive  a single Room Image'
    )
    def retrieve(self, request, *args, **kwargs):
        """Retrive  a single Room Image """
        return super().retrieve(request, *args, **kwargs)
    @swagger_auto_schema(
        operation_summary='Update  a single Room Image'
    )
    def update(self, request, *args, **kwargs):
        """ Update  a single Room Image """
        return super().update(request, *args, **kwargs)
    @swagger_auto_schema(
        operation_summary='Delete  a single Room Image'
    )
    def destroy(self, request, *args, **kwargs):
        """ Delete  a single Room Image """
        return super().destroy(request, *args, **kwargs)
    @swagger_auto_schema(
        operation_summary='patch  a single Room Image'
    )
    def partial_update(self, request, *args, **kwargs):
        """ patch a single Room Image"""
        return super().partial_update(request, *args, **kwargs)


class ReviewViewSet(ModelViewSet):
    serializer_class = ReviewSerializer
    permission_classes = [IsReviewAuthorOrReadonly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        return Review.objects.filter(hotel_id=self.kwargs.get('hotel_pk'))

    def get_serializer_context(self):
        return {'hotel_id': self.kwargs.get('hotel_pk')}
    
    @swagger_auto_schema(
        operation_summary='Retrive all review'
    )
    def list(self, request, *args, **kwargs):
        """Retrive all the review"""
        return super().list(request, *args, **kwargs)
    
    @swagger_auto_schema(
        operation_summary='create a list of review'
    )
    def create(self, request, *args, **kwargs):
        """Only authenticated user can create review"""
        return super().create(request, *args, **kwargs)
    @swagger_auto_schema(
        operation_summary='Retrive  a single review'
    )
    def retrieve(self, request, *args, **kwargs):
        """Retrive  a single review """
        return super().retrieve(request, *args, **kwargs)
    @swagger_auto_schema(
        operation_summary='Update  a single review'
    )
    def update(self, request, *args, **kwargs):
        """ Update  a single review """
        return super().update(request, *args, **kwargs)
    @swagger_auto_schema(
        operation_summary='Delete  a single review'
    )
    def destroy(self, request, *args, **kwargs):
        """ Delete  a single review """
        return super().destroy(request, *args, **kwargs)
    @swagger_auto_schema(
        operation_summary='patch  a single review'
    )
    def partial_update(self, request, *args, **kwargs):
        """ patch a single review"""
        return super().partial_update(request, *args, **kwargs)



class see_num_booking(APIView):
    permission_classes = [IsAdminUser]
    def get(self, request):
        """ show the number of bookings for the week and month."""
        today = now()
        last_week = today - timedelta(days=7)
        last_month = today - timedelta(days=30)

        weekly_bookings = Booking.objects.filter(
            created_at__gte=last_week
        ).count()

        monthly_bookings = Booking.objects.filter(
            created_at__gte=last_month
        ).count()
        return Response({
            "weekly_bookings": weekly_bookings,
            "monthly_bookings": monthly_bookings,})
    
    

class most_booked_room(APIView):
    permission_classes = [IsAdminUser]
    def get(self, request):
        """show the most booked rooms"""
        queryset = (
            room.objects
            .annotate(total=Count('booking_room'))
            .order_by('-total')[:5]
        )
        serializer = mostBookedroomSer(queryset, many=True)
        return Response(serializer.data)

class top_five_user(APIView):
    permission_classes = [IsAdminUser]
    def get(self, request):
        """  show the top five user """
        queryset = (Booking.objects.values('user').annotate(total_bookings=Count('id')).order_by('-total_bookings')[:5])
        serializer = topfiveuser(queryset, many=True)
        return Response(serializer.data)





class cart_bookingviewset(CreateModelMixin, RetrieveModelMixin, DestroyModelMixin, GenericViewSet):
    serializer_class = CartBookingSerializer
    permission_classes = [IsAuthenticated]
    """   this is used for creating cart_booking  """
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        if getattr(self, 'swagger_fake_view', False):
            return Cart_Booking.objects.none()
        return Cart_Booking.objects.prefetch_related('CartBookingRoom__cartRoom').filter(user=self.request.user)
    
    

class Cart_bookingroomViewSet(ModelViewSet):
    http_method_names = ['get', 'post', 'delete']

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return AddbookingroomSerializer
        return bookingroomSerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        if getattr(self, 'swagger_fake_view', False):
            return context

        return {'cartbooking_id': self.kwargs.get('cartbooking_pk')}

    def get_queryset(self):
        return Cart_bookingRoom.objects.select_related('cartRoom').filter(cartbooking_id=self.kwargs.get('cartbooking_pk'))
    @swagger_auto_schema(
        operation_summary='Retrive all Booking Room '
    )
    def list(self, request, *args, **kwargs):
        """Retrive all the Booking Room"""
        return super().list(request, *args, **kwargs)
    
    @swagger_auto_schema(
        operation_summary='create a list of Booking Room'
    )
    def create(self, request, *args, **kwargs):
        """Only authenticated admin can create Booking Room"""
        return super().create(request, *args, **kwargs)
    @swagger_auto_schema(
        operation_summary='Retrive  a single Booking Room'
    )
    def retrieve(self, request, *args, **kwargs):
        """Retrive  a single Booking Room """
        return super().retrieve(request, *args, **kwargs)
    @swagger_auto_schema(
        operation_summary='Update  a single Booking Room'
    )
    def update(self, request, *args, **kwargs):
        """ Update  a single Booking Room """
        return super().update(request, *args, **kwargs)
    @swagger_auto_schema(
        operation_summary='Delete  a single Booking Room'
    )
    def destroy(self, request, *args, **kwargs):
        """ Delete  a single Booking Room """
        return super().destroy(request, *args, **kwargs)



# class Bookingroomsviewset(ModelViewSet):
#     http_method_names = ['get', 'post', 'delete']

#     def get_serializer_class(self):
#         if self.request.method == 'POST':
#             return Addbookingroom_ser
#         return bookingroom_ser
#     def get_serializer_context(self):
#         context = super().get_serializer_context()
#         if getattr(self, 'swagger_fake_view', False):
#             return context

#         return {'booking_id': self.kwargs['booking_pk']}

#     def get_queryset(self):
#         return bookingRoom.objects.select_related('Room').filter(booking_id=self.kwargs['booking_pk'])

class Bookingviewset(ModelViewSet):
    http_method_names = ['get', 'post', 'delete', 'patch', 'head', 'options']
    @swagger_auto_schema(
        operation_summary='to cancel Booking'
    )
    @action(detail=True, methods=['post'])
    def cancel(self, request, pk=None):
        """ to cancel booking"""
        booking = self.get_object()
        BookingService.cancel_booking(booking=booking, user=request.user)
        return Response({'status': 'Booking canceled'})
    @swagger_auto_schema(
        operation_summary='to update status of Booking'
    )
    @action(detail=True, methods=['patch'])
    def update_status(self, request, pk=None):
        """to update booking status"""
        booking = self.get_object()
        serializer = bookingSz.UpdatebookingSer(
            booking, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'status': f'booking status updated to {request.data.get("status")}'})
    
    def get_serializer_class(self):
        if self.action == 'cancel':
            return bookingSz.EmptySerializer
        if self.action == 'create':
            return bookingSz.CreateBookingser
        elif self.action == 'update_status':
            return bookingSz.UpdatebookingSer
        return bookingSz.bookingSer
    
    def get_permissions(self):
        if self.action in ['update_status', 'destroy']:
            return [IsAdminUser()]
        return [IsAuthenticated()]
    
    def get_serializer_context(self):
        if getattr(self, 'swagger_fake_view', False):
            return super().get_serializer_context()
        return {'user_id': self.request.user.id, 'user': self.request.user}
    
    def get_queryset(self):
        if getattr(self, 'swagger_fake_view', False):
            return Booking.objects.none()
        if self.request.user.is_staff:
            return Booking.objects.prefetch_related('rooms__Room').all()
        return Booking.objects.prefetch_related('rooms__Room').filter(user=self.request.user)
    
    @swagger_auto_schema(
        operation_summary='Retrive all Booking'
    )
    def list(self, request, *args, **kwargs):
        """Retrive all the Booking"""
        return super().list(request, *args, **kwargs)
    
    @swagger_auto_schema(
        operation_summary='create a list of Booking'
    )
    def create(self, request, *args, **kwargs):
        """Only authenticated admin can create Booking"""
        return super().create(request, *args, **kwargs)
    @swagger_auto_schema(
        operation_summary='Retrive  a single Booking'
    )
    def retrieve(self, request, *args, **kwargs):
        """Retrive  a single Booking """
        return super().retrieve(request, *args, **kwargs)
    @swagger_auto_schema(
        operation_summary='Update  a single Booking'
    )
    def update(self, request, *args, **kwargs):
        """ Update  a single Booking """
        return super().update(request, *args, **kwargs)
    @swagger_auto_schema(
        operation_summary='Delete  a single Booking'
    )
    def destroy(self, request, *args, **kwargs):
        """ Delete  a single Booking """
        return super().destroy(request, *args, **kwargs)
    @swagger_auto_schema(
        operation_summary='patch  a single Booking'
    )
    def partial_update(self, request, *args, **kwargs):
        """ patch a single Booking"""
        return super().partial_update(request, *args, **kwargs)


