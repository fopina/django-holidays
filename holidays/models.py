from django.db import models
from .utils import list_rules


class Group(models.Model):
    identifier = models.CharField(max_length=10, primary_key=True)
    description = models.CharField(max_length=50)
    parent = models.ForeignKey('self', null=True)

    def __unicode__(self):
        return '%s: %s' % (self.identifier, self.description)


class Rule(models.Model):
    group = models.ForeignKey(Group)
    description = models.CharField(max_length=50)
    method = models.CharField('Rule Type', max_length=50, choices=list_rules())
    parameters = models.CharField(max_length=50, null=True, blank=True)

    def __unicode__(self):
        return '%d: %s' % (self.pk, self.description)
