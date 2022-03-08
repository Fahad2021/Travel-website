from django.db import models


class Package(models.Model):
    name=models.CharField(max_length=200,null=True)
    dec=models.CharField(max_length=200,null=True)
    image=models.ImageField()
    endtime=models.CharField(max_length=200,null=True)

    def __str__(self):
        return self.name

class Hotel(models.Model):
    name=models.CharField(max_length=200,null=True)
    desc=models.CharField(max_length=200,null=True)
    image=models.ImageField()
    booking=models.BooleanField(default=False)
    price=models.CharField(max_length=200,null=True)

    def __str__(self):
        return self.name


