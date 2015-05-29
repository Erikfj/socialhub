from django.db import models
from django.contrib.auth.models import User


class Hub(models.Model):
    username = models.ForeignKey(User, related_name='notes')
    topic = models.CharField(max_length=100)
    hubpoints = models.PositiveIntegerField(default=0)
    created_by = models.ForeignKey(User, related_name="created_notes")
    created_datetime = models.DateTimeField()

    def __unicode__(self):
        return u'%s, %s' % (self.topic, self.hubpoints)

    class Meta:
        ordering = ['-id']

class HubNote(models.Model):
    user = models.ForeignKey(User, related_name='notes_2')
    note = models.TextField()
    points = models.PositiveIntegerField(default=0)
    created_by = models.ForeignKey(User, related_name="created_notes_2")
    created_datetime = models.DateTimeField()

    def __unicode__(self):
        return u'%s' % self.note

    class Meta:
        ordering = ['-id']




