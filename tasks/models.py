from django.db import models

# Create your models here.
class Task(models.Model):

    class Status(models.TextChoices):
        PENDING = "Pending"
        DONE= "Done"
        CANCELLED = "Cancelled"

    title = models.CharField(max_length=250)
    description = models.TextField(blank=True , null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    completed_at = models.DateTimeField(blank=True , null=True)
    status = models.TextField(max_length=20 , choices=Status.choices, default=Status.PENDING)

    def __str__(self) -> str:
        return self.title