from django.db import models

# Create your models here.
class company(models.Model):
    company_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100)
    location=models.CharField(max_length=50)
    about=models.TextField()
    type=models.CharField(max_length=100,
                          choices=(('IT',"INFORMATION TECHNOLOGY")
                                   ,('EE',"ELECTRICAL ENGINEERING"),
                                     ("CE",'COMPUTER ENGINEERING')))
    added_date=models.DateTimeField(auto_now=True)
    active=models.BooleanField(default=True)

    def __str__(self) :
        return self.name + '--'+ self.location
class employee(models.Model):
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=50)
    address=models.CharField(max_length=200)
    phone=models.IntegerField(max_length=10)
    about=models.TextField()
    position=models.CharField(max_length=50,choices=
            (('Manager','Manager'),
             ('Software Developer','Software Developer'),
             ('Project Leader','Project Leader'),
             ('Project Member','Project Member'),
             ('Graphic Designer','Graphic Designer'),   
             ('Non Technical Person','Non Technical Person')     
            ))
    company=models.ForeignKey(company,on_delete=models.CASCADE)