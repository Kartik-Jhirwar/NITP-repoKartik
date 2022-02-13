from email.policy import default
from django.db import models

# Create your models here.

class Data(models.Model):
    college_name = models.CharField(max_length=500)
    img = models.URLField(max_length = 5000 , null=True , default = 0)
    desc = models.CharField(max_length=200 , default = 0 , null=True)

    def __str__(self):
        return self.college_name
