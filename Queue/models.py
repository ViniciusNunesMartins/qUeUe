from django.db import models
from django.contrib.auth.models import User


class Queue(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user")
    employees = models.ManyToManyField(User)
    establishment = models.CharField(max_length=50)
    establishment_closetime = models.TimeField(default=None, null=True, blank=True)

    def __str__(self):
        return self.establishment + ": " + str(self.member_set.count())