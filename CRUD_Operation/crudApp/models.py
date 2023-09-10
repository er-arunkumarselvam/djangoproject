from django.db import models

# Create your models here.
class Employee(models.Model):
#     DEPT = [
#     ("DE", "Developer"),
#     ("DS", "Designer"),
#     ("TE", "Tester"),
#     ("MR", "Manager"),
#     ("TL", "Teamlead"),
# ]
    name = models.CharField(max_length=30)
    age = models.IntegerField()
    # role = models.CharField(max_length=2,choices=DEPT)
    