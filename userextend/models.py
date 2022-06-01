from django.contrib.auth.models import User
from django.db import models

class UserExtend(User):
    gender_choices = (("male", "Male"), ("female", "Female"))

    phone = models.CharField(max_length=15)
    city = models.CharField(max_length=15)
    gender = models.CharField(max_length=10, choices=gender_choices)


    def __str__(self):
        return f"{self.first_name} {self.last_name}"
