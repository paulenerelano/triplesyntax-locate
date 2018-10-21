from django.db import models

class UserLocation(models.Model):
    longitude = models.FloatField()
    latitude = models.FloatField()
    name = models.CharField(max_length=30)

    def __str__(self):
       return str(self.id)

# End UserLocation
