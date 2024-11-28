from django.db import models
from Main_User.models import Main_User_Model

# Create your models here.

class Student_Model(models.Model):
    user = models.ForeignKey(Main_User_Model, on_delete= models.CASCADE )
    Student_name = models.CharField(max_length=255)

    class Meta:
        db_table = 'student_model'

print("Changes made here !!!!!!!")



