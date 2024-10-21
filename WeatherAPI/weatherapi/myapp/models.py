from django.db import models


class Contact(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    comment = models.TextField(max_length=999)
    email = models.EmailField(blank=False)

    class Meta:
        db_table = "contactus"