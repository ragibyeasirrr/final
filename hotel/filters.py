
# from django_filters.rest_framework import FilterSet
# from hotel.models import room


# class roomFilter(FilterSet):
#     class Meta:
#         model = room
#         fields = {
#             'hotel_id': ['exact'],
#             'cost_per_day': ['gt', 'lt']
#         }
import django_filters
from .models import room

class NumberInFilter(django_filters.BaseInFilter, django_filters.NumberFilter):
    pass


class roomFilter(django_filters.FilterSet):

    facility = NumberInFilter(
        field_name="facility__id",
        lookup_expr="in"
    )

    class Meta:
        model = room
        fields = ['hotel', 'facility']