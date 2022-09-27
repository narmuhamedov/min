from django.db import models

class MedicalShows(models.Model):
    TYPE_IMG = (
        ('HEART', "HEART"),
        ('KIDNEYS', 'KIDNEYS'),
        ("LIVER", "LIVER"),
        ('EYES', 'EYES')
    )
    title = models.CharField(max_length=100)
    description = models.TextField()
    images = models.ImageField(upload_to='')
    type = models.CharField(choices=TYPE_IMG, max_length=100)
    timeadd = models.DateTimeField()

    def __str__(self):
        return self.title

