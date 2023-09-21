from django.db import models

# Create your models here.
class Virtual_Id(models.Model):
    img=models.ImageField(upload_to='Images',blank='True',null='True')
    Name=models.CharField(max_length=50)
    Emp_id=models.BigIntegerField()
    Contact=models.BigIntegerField()
    Designation=models.CharField(max_length=50)
    def __str__(self):
        return self.Name