from django.db import models
from profiles.models import Profile


class Property(models.Model):
    PROPERTY_TYPES = [
        ('PG', 'Paying Guest (PG)'),
        ('Flat', 'Flat'),
        ('Independent', 'Independent'),
        ('Land', 'Land'),
        ('Building', 'Building'),
    ]
    TRANSACTION_TYPES = [
        ('Rent', 'Rent'),
        ('Lease', 'Lease'),
        ('Sale', 'Sale'),
    ]
    user_profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    property_type = models.CharField(max_length=20, choices=PROPERTY_TYPES)
    transaction_type = models.CharField(max_length=20, choices=TRANSACTION_TYPES)
    bhk = models.PositiveIntegerField()
    address = models.TextField(max_length=250)
    picture1 = models.ImageField(upload_to='assets/property_pictures')
    picture2 = models.ImageField(upload_to='assets/property_pictures', null=True, blank=True)
    picture3 = models.ImageField(upload_to='assets/property_pictures', null=True, blank=True)
    description = models.TextField(max_length=1000)
    price = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.property_type} | {self.transaction_type} | {self.address}'


class Service(models.Model):
    user_profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    title = models.CharField(max_length=70)
    country = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    available_location = models.CharField(max_length=20)
    google_profile = models.URLField(null=True, blank=True)

    def __str__(self):
        return f'{self.title} | {self.available_location} | {self.city}'
