from django.db import models
from django.utils import timezone

# Create your models here.


class TalkingsOn(models.Model):
    boast_roast = [(True, "boast"), (False, "roast")]
    body = models.CharField(max_length=280)
    choices = models.BooleanField(choices=boast_roast, default=True)
    up_vote = models.IntegerField(default=0)
    down_vote = models.IntegerField(default=0)
    post_date = models.DateTimeField(default=timezone.now)
    # s_key = models.CharField(max_length=6)

    @property
    def votes(self):
        return self.up_vote - self.down_vote

