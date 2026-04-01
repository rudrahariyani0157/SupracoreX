from django.db import models

class getyourwebsitedata(models.Model):
    name = models.CharField(max_length=32)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    budget_range = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.name