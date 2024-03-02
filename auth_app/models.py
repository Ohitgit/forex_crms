from django.db import models

# Create your models here.
class BaseModel(models.Model):
    added_on = models.DateTimeField(default=timezone.now)
    updated_on = models.DateTimeField(auto_now=True)
    class Meta:
        abstract = True

