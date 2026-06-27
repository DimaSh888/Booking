from django.db import models
from django.contrib.auth.models import User


class Room(models.Model):
    number = models.IntegerField()
    capacity = models.IntegerField()
    location = models.CharField(max_length=150)
    description = models.TextField()

    class Meta:
        pass

    def __str__(self):
        return f"{str(self.number)}, {self.location}, {self.description}"


class Booking(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="bookings")
    room = models.ForeignKey(
        Room, on_delete=models.CASCADE, related_name="bookings")
    start_time = models.DateTimeField(auto_now=False, auto_now_add=False)
    end_time = models.DateTimeField(auto_now=False, auto_now_add=False)
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)

    class Meta:
        pass

    def __str__(self):
        return f"{self.user.username} - {self.room}"
