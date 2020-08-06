from django.db import models


class Client(models.Model):

    full_name = models.CharField(max_length=200, default='')
    run = models.CharField(max_length=15, default='')
    address = models.CharField(max_length=400, default='')
    profession = models.CharField(max_length=100, default='')
    nationality = models.CharField(max_length=100, default='')

    class Meta:
        db_table = 'client'


class Institution(models.Model):
    
    business_name = models.CharField(max_length=200, default='')
    rut = models.CharField(max_length=15, default='')
    address = models.CharField(max_length=400, default='')
    name_of_legal_representative = models.CharField(max_length=100, default='')

    class Meta:
        db_table = 'institution'


class HealthPlan(models.Model):

    name = models.CharField(max_length=200)

    class Meta:
        db_table = 'health_plan'



