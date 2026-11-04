from django.db import models

class Person(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.full_name

class Dog(models.Model):
    description = models.TextField()
    birth_date = models.DateField()
    weight_kg = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return str(self.birth_date)

class Cat(models.Model):
    lives_left = models.IntegerField()
    speed_kmh = models.FloatField()
    profile_url = models.URLField()

    def __str__(self):
        return str(self.speed_kmh)