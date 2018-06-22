from django.db import models

# Create your models here.

class qadmin(models.Model):
    User_name = models.CharField(max_length=100,default='admin')
    Passwd = models.CharField(max_length=100,default="admin")

    def __str__(self):
        return self.User_name