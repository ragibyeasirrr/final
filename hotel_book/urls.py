"""
URL configuration for hotel_book project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
# from hotel.views import hotelviewset,hotel_cat_viewset,room_viewset,room_fac_viewset,room_img_viewset
from hotel.views import hotel_cat_viewset,hotelviewset,room_viewset,room_fac_viewset,room_img_viewset,ReviewViewSet,reviewViewSet,Bookingviewset,cart_bookingviewset,Cart_bookingroomViewSet,see_num_booking,most_booked_room, top_five_user,initiate_payment,payment_cancel,payment_fail,payment_success

from rest_framework_nested import routers
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
    openapi.Info(
        title="Hotel Booking",
        default_version='v1',
        description="API Documentation for Hotel Booking Project",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@phimart.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)




router = routers.DefaultRouter()
router.register("hotel_category",hotel_cat_viewset,basename='hotel_category')
router.register("hotel",hotelviewset,basename='hotel')
router.register("room",room_viewset,basename='room')
router.register("room_facility",room_fac_viewset,basename='room_facility')
# router.register("room_Img",room_img_viewset,basename='room_Img')

router.register("bookings",Bookingviewset,basename='booking')
router.register("cart_booking",cart_bookingviewset,basename='cart_bookings')
hotel_router = routers.NestedDefaultRouter(
    router, 'hotel', lookup='hotel')
room_router = routers.NestedDefaultRouter(
    router, 'room', lookup='room')
room_router.register('rev', reviewViewSet, basename='room-review')
cartbooking_router = routers.NestedDefaultRouter(
    router, 'cart_booking', lookup='cartbooking')
hotel_router.register('reviews', ReviewViewSet, basename='hotel-review')
roomimg_router=routers.NestedDefaultRouter(
    router, 'room', lookup='rooms')
cartbooking_router.register('bookingroom',Cart_bookingroomViewSet,basename='booking_room')
roomimg_router.register('roomimg',room_img_viewset,basename='roomImg')
urlpatterns = [
    path('', include(router.urls)),
    path('', include(hotel_router.urls)),
    path('', include(cartbooking_router.urls)),
    path('', include(room_router.urls)), 
    path('', include(roomimg_router.urls)), 
    path('payment/initiate/', initiate_payment),
    path('payment/success/', payment_success),
    path('payment/cancel/', payment_cancel),
    path('payment/fail/', payment_fail),
    path('admin/', admin.site.urls),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    path('seebooking/', see_num_booking.as_view()),
    path('mostbookedroom/', most_booked_room.as_view()),
    path('topfiveuser/',  top_five_user.as_view()),
     path('swagger/', schema_view.with_ui('swagger',
         cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc',
         cache_timeout=0), name='schema-redoc'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
