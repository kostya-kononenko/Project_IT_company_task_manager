from django.contrib.auth.models import AbstractUser
from django.db import models


class Position(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Worker(AbstractUser):
    position = models.ForeignKey(Position, on_delete=models.CASCADE, null=True)

    class Meta:
        verbose_name = "worker"
        verbose_name_plural = "workers"

    def __str__(self):
        return f"{self.username} ({self.first_name} {self.last_name})"


class TaskType(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Task(models.Model):
    class Priority(models.TextChoices):
        low = "low", "low"
        medium = "medium", "medium"
        high = "high", "high"
        very_high = "very high", "very high"

    name = models.CharField(max_length=255)
    descriptions = models.CharField(max_length=255)
    deadline = models.DateField()
    is_completed = models.BooleanField(default=False)
    priority = models.CharField(max_length=9, choices=Priority.choices, default=Priority.low)
    task_type = models.ForeignKey(TaskType, on_delete=models.CASCADE)
    assignees = models.ManyToManyField(Worker, related_name="workers")

    def __str__(self):
        return f"{self.name} {self.descriptions} {self.deadline}"

    class Meta:
        ordering = ["name"]
