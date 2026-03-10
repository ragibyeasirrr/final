

import django_filters
from .models import room


class NumberInFilter(django_filters.BaseInFilter, django_filters.NumberFilter):
    pass


class roomFilter(django_filters.FilterSet):

    facility = NumberInFilter(
        field_name="facility__id",
        lookup_expr="in"
    )

    cost_per_day__gt = django_filters.NumberFilter(
        field_name="cost_per_day",
        lookup_expr="gt"
    )

    cost_per_day__lt = django_filters.NumberFilter(
        field_name="cost_per_day",
        lookup_expr="lt"
    )

    class Meta:
        model = room
        fields = [
            "hotel",
            "facility",
            "cost_per_day__gt",
            "cost_per_day__lt"
        ]