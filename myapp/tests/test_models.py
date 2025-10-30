from datetime import date, time, timedelta

import pytest
from django.core.exceptions import ValidationError

from myapp.models import Booking, Table


@pytest.mark.django_db
def test_past_date_rejected(django_user_model):
    u = django_user_model.objects.create_user("u", "u@u.com", "pw")
    t = Table.objects.create(name="T1", seats=2)
    b = Booking(
        user=u,
        date=date.today() - timedelta(days=1),
        time=time(18, 0),
        party_size=2,
        table=t,
    )
    with pytest.raises(ValidationError):
        b.full_clean()


@pytest.mark.django_db
def test_capacity_limit_enforced(django_user_model):
    u = django_user_model.objects.create_user("u", "u@u.com", "pw")
    t = Table.objects.create(name="T1", seats=2)
    b = Booking(user=u, date=date.today(), time=time(18, 0), party_size=3, table=t)
    with pytest.raises(ValidationError):
        b.full_clean()


@pytest.mark.django_db
def test_double_booking_blocked(django_user_model):
    u = django_user_model.objects.create_user("u", "u@u.com", "pw")
    t = Table.objects.create(name="T1", seats=2)
    Booking.objects.create(
        user=u, date=date.today(), time=time(18, 0), party_size=2, table=t
    )
    b2 = Booking(user=u, date=date.today(), time=time(18, 0), party_size=2, table=t)
    with pytest.raises(ValidationError):
        b2.full_clean()
