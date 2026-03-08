from django.db import models

class Decision(models.Model):
    text = models.TextField()
    risk_level = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text[:50]