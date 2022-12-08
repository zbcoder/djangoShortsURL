from django.db import models
from  django.contrib.auth.models import User

# Create your models here.
class Links(models.Model):
    link_id = models.AutoField(primary_key=True)
    full_url = models.TextField(max_length=255)
    cut_url = models.TextField(max_length=30)
    user = models.ForeignKey(User, models.CASCADE, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'links'
