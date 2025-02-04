from django.db import models
from django.core.exceptions import ValidationError
import datetime
from users.models import User
from cloudinary.models import CloudinaryField


# Create your models here.
class Service(models.Model):
    """
    Stores a single service provided by Perfect Paws
    """
    name = models.CharField('service name', max_length=200)
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    active = models.BooleanField(default=False)
    duration = models.PositiveIntegerField('service duration (in minutes)')
    image = CloudinaryField('image', default='placeholder')
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name}"

    @property
    def appointment_length(self):
        return "long" if self.duration > 60 else "short"

    def clean(self):
        super().clean()
        if self.cost < 0.0:
            raise ValidationError({'cost': 'Cost cannot be less than 0'})
        if self.duration > 480:
            raise ValidationError({'duration': "Duration cannot be longer than 480 minutes (8 hours)"})


class Booking(models.Model):
    """
    Stores a single booking record
    """

    class AppointmentTimes(datetime.time, models.Choices):
        EIGHT_THIRTY = 8, 30, "8:30"
        NINE = 9, 0, "9:00"
        TEN = 10, 0, "10:00"
        ELEVEN = 11, 0, "11:00"
        TWELVE = 12, 0, "12:00"
        ONE_THIRTY = 13, 30, "13:30"
        TWO = 14, 0, "14:00"
        THREE = 15, 0, "15:00"
        FOUR = 16, 0, "16:00"
    
    class DogSizes(models.IntegerChoices):
        LARGE = 0, "Large (>25kg)"
        MEDIUM = 1, "Medium (10-25kg)"
        SMALL = 2, "Small (<10kg)"
    
    client = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='bookings'
    )
    service = models.ForeignKey(
        Service, on_delete=models.CASCADE, related_name='appointments'
    )
    date = models.DateField()
    time = models.TimeField(choices=AppointmentTimes.choices)
    dog_name = models.CharField("dog's name", max_length=150)
    dog_breed = models.CharField("dog's breed", max_length=150)
    dog_size = models.IntegerField("dog's size", choices=DogSizes.choices, default=DogSizes.LARGE)
    additional_notes = models.TextField(blank=True)
    canceled = models.BooleanField("canceled?", default=False)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date', 'time']
    
    def __str__(self):
        return f"{self.service.name} for {self.dog_name} [{self.date} {self.time}]"

    def clean(self):
        super().clean()

        # determine if the time selected is appropriate for this service type
        if self.service.appointment_length:
            valid_choices = [
                '08:30',
                '11:00',
                '13:30',
                '14:00',
            ]
        else:
            valid_choices = [
                '09:00',
                '10:00',
                '11:00',
                '12:00',
                '14:00',
                '15:00',
                '16:00',
            ]
        
        if self.time not in [datetime.datetime.strptime(v, '%H:%M').time() for v in valid_choices]:
            print('failed at this point', self.time, valid_choices)
            raise ValidationError("Invalid time selected for service type")

        queryset = Booking.objects.filter(
            date=self.date,
            time=self.time,
            canceled=False,
        )

        if queryset.exists():
            if self.service.appointment_length in [b.service.appointment_length for b in queryset if b.service.active]:
                raise ValidationError("Cannot create booking, that timeslot is already booked")
        
        if self.date.weekday in [0, 6]:
            raise ValidationError({'date': "Date cannot be Monday or Sunday"})
