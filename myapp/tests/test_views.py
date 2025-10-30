import pytest
from django.urls import reverse
from datetime import date, time
from myapp.models import Table, Booking

@pytest.mark.django_db
def test_login_required_for_reserve(client):
    resp = client.get(reverse("reserve"))
    assert resp.status_code in (302, 301)

@pytest.mark.django_db
def test_owner_can_edit_own_booking(client, django_user_model):
    u = django_user_model.objects.create_user("u","u@u.com","pw")
    client.login(username="u", password="pw")
    t = Table.objects.create(name="T1", seats=2)
    b = Booking.objects.create(user=u, date=date.today(), time=time(18,0), party_size=2, table=t)
    resp = client.get(reverse("booking_edit", args=[b.pk]))
    assert resp.status_code == 200
