from django.db import models

class FaultReport(models.Model):
    FAULT_TYPES = [
        ('electricity', 'Electricity'),
        ('water', 'Water'),
        ('road', 'Road'),
        ('other', 'Other'),
    ]
    fault_type = models.CharField(max_length=20, choices=FAULT_TYPES)
    description = models.TextField(blank=True)
    location = models.CharField(max_length=200)
    status = models.CharField(max_length=50, default='Submitted')
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.fault_type} – {self.location}"
