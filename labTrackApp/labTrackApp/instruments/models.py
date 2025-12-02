from django.db import models

STATUS = [
    ('operational', 'Operational'),
    ('under_maintenance', 'Under Maintenance'),
    ('service', 'Validation'),
]
class Instrument(models.Model):
    brand = models.CharField(
        max_length=30
    )

    model = models.CharField(
        max_length=30
    )

    serial_number = models.CharField(
        max_length=50
    )

    description = models.TextField(
        max_length = 150
    )

    status = models.CharField(
        max_length=20,
        choices= STATUS,
        default='operational',
    )

    

    def __str__(self):
        return self.model

