from django.db import models


class Report(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.IntegerField()
    name = models.CharField(max_length=125)
    username = models.CharField(max_length=50)
    email = models.CharField(max_length=125)
    address = models.TextField()
    phone = models.CharField(max_length=15)
    website = models.CharField(max_length=125)
    company = models.TextField()
    title = models.CharField(max_length=125)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "report"