from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=63, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]


class Task(models.Model):
    content = models.CharField(max_length=400)
    datetime = models.DateTimeField(auto_now_add=True)
    deadline = models.DateField(blank=True, null=True)
    is_completed = models.BooleanField(default=False)
    tags = models.ManyToManyField(Tag, blank=True, related_name="tasks")
