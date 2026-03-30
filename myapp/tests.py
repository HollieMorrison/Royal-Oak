from datetime import timedelta

from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from .forms import BookingForm
from .models import Booking, Table

User = get_user_model()


class BookingModelTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="hollie", password="testpass123")
        self.table = Table.objects.create(name="Table 1", seats=4)

    def test_booking_string_representation(self):
        booking = Booking.objects.create(
            user=self.user,
            table=self.table,
            date=timezone.localdate() + timedelta(days=1),
            time="18:00",
            party_size=2,
        )
        self.assertIn("Table 1", str(booking))

    def test_booking_cannot_be_in_past(self):
        booking = Booking(
            user=self.user,
            table=self.table,
            date=timezone.localdate() - timedelta(days=1),
            time="18:00",
            party_size=2,
        )
        with self.assertRaises(ValidationError):
            booking.full_clean()

    def test_booking_cannot_exceed_table_capacity(self):
        booking = Booking(
            user=self.user,
            table=self.table,
            date=timezone.localdate() + timedelta(days=1),
            time="18:00",
            party_size=6,
        )
        with self.assertRaises(ValidationError):
            booking.full_clean()

    def test_booking_cannot_double_book_same_slot(self):
        Booking.objects.create(
            user=self.user,
            table=self.table,
            date=timezone.localdate() + timedelta(days=1),
            time="18:00",
            party_size=2,
        )
        second_booking = Booking(
            user=self.user,
            table=self.table,
            date=timezone.localdate() + timedelta(days=1),
            time="18:00",
            party_size=2,
        )
        with self.assertRaises(ValidationError):
            second_booking.full_clean()


class BookingFormTests(TestCase):
    def setUp(self):
        self.table = Table.objects.create(name="Table 2", seats=4)

    def test_form_rejects_past_date(self):
        form = BookingForm(data={
            "table": self.table.id,
            "date": timezone.localdate() - timedelta(days=1),
            "time": "18:00",
            "party_size": 2,
        })
        self.assertFalse(form.is_valid())

    def test_form_rejects_party_size_above_table_capacity(self):
        form = BookingForm(data={
            "table": self.table.id,
            "date": timezone.localdate() + timedelta(days=1),
            "time": "18:00",
            "party_size": 6,
        })
        self.assertFalse(form.is_valid())

    def test_form_accepts_valid_booking(self):
        form = BookingForm(data={
            "table": self.table.id,
            "date": timezone.localdate() + timedelta(days=1),
            "time": "18:00",
            "party_size": 2,
        })
        self.assertTrue(form.is_valid())


class BookingViewTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="hollie", password="testpass123")
        self.other_user = User.objects.create_user(username="other", password="testpass123")
        self.table = Table.objects.create(name="Table 3", seats=4)
        self.booking = Booking.objects.create(
            user=self.user,
            table=self.table,
            date=timezone.localdate() + timedelta(days=1),
            time="18:00",
            party_size=2,
        )

    def test_reserve_requires_login(self):
        response = self.client.get(reverse("reserve"))
        self.assertEqual(response.status_code, 302)

    def test_my_bookings_requires_login(self):
        response = self.client.get(reverse("my_bookings"))
        self.assertEqual(response.status_code, 302)

    def test_logged_in_user_can_create_booking(self):
        self.client.login(username="hollie", password="testpass123")
        response = self.client.post(reverse("reserve"), {
            "table": self.table.id,
            "date": timezone.localdate() + timedelta(days=2),
            "time": "19:00",
            "party_size": 2,
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Booking.objects.filter(user=self.user).count(), 2)

    def test_user_only_sees_own_bookings(self):
        Booking.objects.create(
            user=self.other_user,
            table=self.table,
            date=timezone.localdate() + timedelta(days=2),
            time="20:00",
            party_size=2,
        )
        self.client.login(username="hollie", password="testpass123")
        response = self.client.get(reverse("my_bookings"))
        self.assertContains(response, "18:00")
        self.assertNotContains(response, "20:00")

    def test_user_can_edit_own_booking(self):
        self.client.login(username="hollie", password="testpass123")
        response = self.client.post(reverse("booking_edit", args=[self.booking.pk]), {
            "table": self.table.id,
            "date": timezone.localdate() + timedelta(days=1),
            "time": "19:30",
            "party_size": 2,
        })
        self.assertEqual(response.status_code, 302)
        self.booking.refresh_from_db()
        self.assertEqual(str(self.booking.time), "19:30:00")

    def test_user_cannot_edit_someone_elses_booking(self):
        self.client.login(username="other", password="testpass123")
        response = self.client.get(reverse("booking_edit", args=[self.booking.pk]))
        self.assertEqual(response.status_code, 404)

    def test_user_can_delete_own_booking(self):
        self.client.login(username="hollie", password="testpass123")
        response = self.client.post(reverse("booking_delete", args=[self.booking.pk]))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Booking.objects.filter(pk=self.booking.pk).exists())
