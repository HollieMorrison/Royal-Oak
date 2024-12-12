from django.db import models
from django.utils.translation import gettext_lazy as _

# Reservation model...

class Reservation( models.Model ):
    name = models.CharField(max_length=100)
    date = models.DateField()
    time = models.TimeField()
    party_size = models.IntegerField()
    children = models.IntegerField()
    dietaryNotes = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.name} - { self.date} at {self.time} for {self.party_size} with {self.children}. dietary included {self.dietaryNotes}"
    

# Menu type ( starter , main, side , dessert )
class MealType(models.TextChoices):
     BREAKFAST = 'breakfast', _('Breakfast')
     LUNCH = 'lunch', _('Lunch')
     DINNER = 'dinner', _('Dinner')

# Menu model 

class Menu ( models.Model ):
       name = models.CharField(max_length=100) 
       price = models.FloatField()
       type = models.CharField(choices= MealType.choices, default=MealType.LUNCH , max_length=30 )

       def __str__(self):
            return f"{self.name} at £{self.price} type {self.type}"