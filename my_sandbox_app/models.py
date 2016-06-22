from __future__ import unicode_literals

from django.db import models
from django.core.validators import RegexValidator, MaxValueValidator, MinValueValidator
from string import capitalize

numeric = RegexValidator(r'^[0-9]*$', 'Only numeric characters are allowed.')

class TriStatePlace(models.Model):
    STATES = (
               ("nj", "New Jersey"),
               ("ny", "New York"),
               ("ct", "Connecticut"),
            )
    
    city = models.CharField(max_length = 25)
    state = models.CharField(max_length = 20, choices = STATES)
    zip = models.CharField(max_length = 5, validators=[numeric])
    
    def __unicode__(self):
        return capitalize(self.city) + ", " + (self.state.upper())
    
class Resident(models.Model):
    location = models.ForeignKey(TriStatePlace)
    first_name = models.CharField(max_length = 30)
    last_name = models.CharField(max_length = 30)
    age = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(99)])
    
    class Meta:
        ordering = ["-age"]
