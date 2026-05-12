from django.db import migrations, models
from django.contrib.auth.models import User
from django.utils import timezone

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)
    # यह नई लाइन जोड़ें
    date_due = models.DateField(default=timezone.now)

    def __str__(self):
        return self.title


