from django.db import models
from datetime import time

# Create your models here.



class Room (models.Model):
    name = models.CharField(max_length=200, default=" ")
    room_floor= models.IntegerField( default="1")
    room_num =models.IntegerField(default="0")

    def __str__(self):
        return f"{self.name}: number {self.room_num} on the {self.room_floor} st/nd/th floor"


class Meeting(models.Model):
    title = models.CharField(max_length=200)
    date =models.DateField()
    start_time=models.TimeField(default=time(9))
    duration = models.IntegerField(default=2)
    decription = models.TextField(max_length=1500, default=( 'Add description here '))
    room = models.ForeignKey(Room, on_delete=models.CASCADE)


    def __str__(self):
        return f"{self.title} at {self.start_time} on {self.date}"


