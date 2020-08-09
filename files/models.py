from django.db import models


class Client(models.Model):

    full_name = models.CharField(max_length=200, default='')
    run = models.CharField(max_length=15, default='')
    address = models.CharField(max_length=400, default='')
    profession = models.CharField(max_length=100, default='')
    nationality = models.CharField(max_length=100, default='')

    class Meta:
        db_table = 'client'

    def get_as_dict(self):
        return {
            'full_name': self.full_name,
            'run': self.run,
            'address': self.address,
            'profession': self.profession,
            'nationality': self.nationality,
        }


class Institution(models.Model):
    
    business_name = models.CharField(max_length=200, default='')
    rut = models.CharField(max_length=15, default='')
    address = models.CharField(max_length=400, default='')
    name_of_legal_representative = models.CharField(max_length=100, default='')

    class Meta:
        db_table = 'institution'

    def get_as_dict(self):
        return {
            'business_name': self.business_name,
            'rut': self.rut,
            'address': self.address,
            'name_of_legal_representative': self.name_of_legal_representative,
        }


class HealthPlan(models.Model):

    name = models.CharField(max_length=200)

    class Meta:
        db_table = 'health_plan'


class Writing(models.Model):

    name = models.CharField(max_length=200)
    content = models.TextField()

    class Meta:
        db_table = 'writing'