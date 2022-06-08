from django.db import models
from datetime import time
import uuid

# Create your models here.
class Room(models.Model):
    name = models.CharField(max_length=50)
    floor_number = models.IntegerField(default=1)
    room_number = models.IntegerField(default=5)

    def __str__(self):
        return f"{self.name}: room {self.room_number} on floor {self.floor_number}"

class Meeting(models.Model):
    slug = models.SlugField(unique=True, default=uuid.uuid1)
    title = models.CharField(max_length=200)
    date = models.DateField()
    start_time = models.TimeField(default=time(9))
    duration = models.IntegerField(default=1)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} at {self.start_time} on {self.date}"

