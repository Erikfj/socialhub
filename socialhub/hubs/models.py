from django.db import models
from django.contrib.auth.models import User


class Hub(models.Model):
    username = models.ForeignKey(User, related_name='notes')
    topic = models.CharField(max_length=100)
    hubpoints = models.PositiveIntegerField(default=0)
    created_by = models.ForeignKey(User, related_name="created_notes")
    created_datetime = models.DateTimeField()

    def __unicode__(self):
        return u'%s (%s)' % (self.topic, self.message)


class HubNote(models.Model):
    user = models.ForeignKey(User, related_name='notes_2')
    note = models.TextField()
    points = models.PositiveIntegerField(default=0)
    created_by = models.ForeignKey(User, related_name="created_notes_2")
    created_datetime = models.TextField()

    def __unicode__(self):
        return u'%s' % self.note

    class Meta:
        ordering = ['-id']




