from django.db import models


class Task(models.Model):
    description = models.CharField(max_length=140)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-timestamp']

    def __unicode__(self):
        return self.description
