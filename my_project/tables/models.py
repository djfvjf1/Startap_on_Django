from django.db import models


# Create your models here.
class Table(models.Model):
    author_name = models.CharField( max_length=100 )
    patent = models.CharField( max_length=100)
    year = models.CharField( max_length=100)
    title = models.CharField( max_length=100)

    def publish(self):
        self.save()

    def __str__(self):
        return self.title
    
class Table23(models.Model):
     subject = models.CharField(max_length=100)
     name_of_partner = models.CharField(max_length=100)
     date_of_contract = models.CharField(max_length=40)
     start_date = models.CharField(max_length=40)
     end_date = models.CharField(max_length=40)
     availability = models.CharField(max_length=100)

     def publish(self):
        self.save()

     def __str__(self):
        return self.availability
     
class Table26(models.Model):
     organisation = models.CharField(max_length=100)
     subject_of_contract = models.CharField(max_length=100)
     directon_of_speciality = models.CharField(max_length=40)
     date = models.CharField(max_length=40)
     terms_of_the_contract = models.CharField(max_length=40)

     def publish(self):
        self.save()

     def __str__(self):
        return self.terms_of_the_contract
