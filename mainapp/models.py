from django.db import models

# Create your models here.
class Website(models.Model):
    url_name      = models.CharField(max_length=100)
    code_name     = models.CharField(max_length=50)
    total_count   = models.IntegerField()
   
    
    def __str__(self):
        return  str(self.url_name)


class PageVisit(models.Model):
    page_name = models.CharField(max_length=255)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    duration = models.IntegerField()
