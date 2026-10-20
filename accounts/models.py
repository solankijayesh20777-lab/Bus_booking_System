from django.db import models

# Create your models here.

class Login(models.Model):

    #Add Field name
    username = models.CharField( max_length=150,unique = True)
    password = models.CharField(max_length=180)

    class Meta:
        db_table = 'login' # Create a table mysql
        db_table = 'registration'

    def _str_(self):
        return self.username
    
