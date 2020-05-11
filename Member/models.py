from django.db import models
from django.utils import timezone
from Queue.models import Queue
from django.utils.translation import ugettext_lazy as _
import uuid
import datetime

class Member(models.Model):
  session = models.CharField(max_length = 50, unique=True)
  queue = models.ForeignKey(Queue, on_delete = models.CASCADE)
  priority = models.BooleanField(default = False)
  create_at = models.DateTimeField(default = timezone.now)

  def __str__(self):
    position = self.position()
    #s = "(" + str(self.pk) + ", " + str(self.queue.pk) + ") " + str(self.priority) + " " + str(self.create_at) + " "
    s = ""
    if position == 0:
      return s + "Is you!"
    else:
      return s + "Position: " + str(position) + "º"


  def position(self):
    _set = self.queue.member_set.all().order_by('-priority', 'create_at')

    for i in range(len(_set)):
      if _set[i].pk == self.pk:
        return i
    raise ValueError

    # def recursive_search(index, begin, end):
    #   middle = (begin + end) // 2
    #   if begin > end:
    #     raise ValueError
    #   elif index == _set[middle].pk:
    #     return middle
    #   elif index < _set[middle].pk:
    #     return recursive_search(index, begin, middle - 1)
    #   else:
    #     return recursive_search(index, middle + 1, end)
    # return recursive_search(self.pk, 0, len(_set) - 1)