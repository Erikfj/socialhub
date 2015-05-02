from django.db import models
from django.contrib.auth.models import User

class HubNote(models.Model):
	user = models.ForeignKey(User, related_name='notes')
	note = models.TextField()
	points = models.PositiveIntegerField(default=0)
	created_by = models.ForeignKey(User, related_name="created_notes")
	created_datetime = models.DateTimeField()

	def __unicode__(self):
		return u'%s' % self.note

		class Meta:
			ordering = ['-id']