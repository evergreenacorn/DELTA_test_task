from django.db import models

class CommonEntity(models.Model):
    name = models.CharField(max_length=255, unique=True, blank=False, null=False)

    class Meta:
        abstract = True

    def __str__(self):
        return f"{self.pk}: {self.name}"
