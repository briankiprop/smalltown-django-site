from django.db import models

# Create your models here.
class notices(models.Model):
    pdf_file=models.FileField(upload_to='notices',null=False)
    description=models.TextField()

class news_updates(models.Model):
    headline=models.CharField(max_length=100)
    date_time=models.DateTimeField(auto_now=True,auto_created=True)
    image=models.ImageField(upload_to='news_images',null=False)
    body=models.TextField()
    author=models.CharField(max_length=50,null=True,default='null')

class events_model(models.Model):
    date=models.DateField(auto_created=True,auto_now=True)
    location=models.CharField(max_length=20)
    headline=models.CharField(max_length=50)
    image=models.ImageField(upload_to='events_images')
    description=models.TextField(default='',null=True,)

    def __unicode__(self):
        return self.headline
