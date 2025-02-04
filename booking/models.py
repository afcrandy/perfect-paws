import datetime
from django.db import models
from django.core.exceptions import ValidationError
from cloudinary.models import CloudinaryField
from users.models import User


# Create your models here.
class Service(models.Model):
    """
    Models a grooming service offered by the business.
    
    **Attributes:**
        name (str): The name of the service.
        cost (Decimal): The cost of the service.
        description (str): A description of the service.
        active (bool): Whether the service is currently active.
        duration (int): The duration of the service in minutes.
        image (CloudinaryField): Image representing the service.
        created_on (datetime): Timestamp for when the service was created.
    
    **Methods:**
        appointment_length: Returns 'long' or 'short' based on service duration.
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
        """
        Returns 'long' if the service duration is more than 60 minutes, else 'short'.
        """
        return "long" if self.duration > 60 else "short"

    def clean(self):
        """
        Validates the service's fields:
            - Ensures the cost is not negative.
            - Ensures the duration does not exceed 480 minutes (8 hours).
        """
        super().clean()
        if self.cost < 0.0:
            raise ValidationError({'cost': 'Cost cannot be less than 0'})
        if self.duration > 480:
            raise ValidationError({'duration': "Duration cannot be longer than 480 minutes (8 hours)"})


class Booking(models.Model):
    """
    Models a booking for a grooming service.
    
    **Attributes:**
        client (ForeignKey): The :model:`users.User` making the booking.
        service (ForeignKey): The :model:`booking.Service` being booked.
        date (Date): The date of the booking.
        time (Time): The time of the booking.
        dog_name (str): The name of the dog being groomed.
        dog_breed (str): The breed of the dog.
        dog_size (int): The size category of the dog.
        additional_notes (str): Any additional information for the booking.
        canceled (bool): Whether the booking was canceled.
        created_on (datetime): Timestamp for when the booking was created.
    
    **Meta:**
        ordering: Orders bookings by date and time.
    
    **Methods:**
        clean: Validates that the booking time is appropriate for the service and checks availability.
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
        """
        Validates the booking:
            - Ensures the selected time is valid for the service type.
            - Ensures the selected time slot is not already booked.
            - Ensures the date is not on a Sunday or Monday.
        """
        super().clean()

        # determine if the time selected is appropriate for this service type
        if self.service.appointment_length == 'long':
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
