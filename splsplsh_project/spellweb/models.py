from datetime import datetime

from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import localtime

class Teacher(models.Model):
    user = models.OneToOneField(User, primary_key=True)
    chosen_name = models.CharField(max_length=30)
    family_name = models.CharField(max_length=30)

    class Meta:
        ordering = ['family_name', 'chosen_name']

    def __unicode__(self):
        return u'%s, %s' % (self.family_name, self.chosen_name)

class Learner(models.Model):
    #The username property is a temporary thing until
    #I've worked out how to extend django-registration
    #to do this properly. Clearly the null=True is not good !
    username = models.CharField(max_length=30, null=True)
    teacher = models.ForeignKey(Teacher)
    chosen_name = models.CharField(max_length=30)
    family_name = models.CharField(max_length=30)
    learning_level = models.IntegerField(default=0)

    class Meta:
        ordering = ['family_name', 'chosen_name']

    def __unicode__(self):
        return u'%s, %s' % (self.family_name, self.chosen_name)

class Word(models.Model):
    ESSENTIALWORDS = 'EW'
    NZCER = 'ER'
    OTHER = 'OT'
    WORDSOURCE_TYPE_CHOICES = (
        (ESSENTIALWORDS, 'Essential Words'),
        (NZCER, 'NZCER'),
        (OTHER, 'OTHER'),
    )

    level = models.IntegerField()
    word = models.CharField(max_length=30)
    source = models.CharField(max_length=2,
                              choices=WORDSOURCE_TYPE_CHOICES,
                              default=OTHER)
    hint = models.CharField(max_length=30, null=True, blank=True)

    class Meta:
        ordering = ['level', 'word']
        unique_together = (("source", "word"),)

    def __unicode__(self):
        return self.word

    

class Attempt(models.Model):
    learner = models.ForeignKey(Learner)
    word = models.ForeignKey(Word)
    when = models.DateTimeField(auto_now_add=True)
    success = models.BooleanField(default=False)

    class Meta:
        ordering = ['-when']

    def __unicode__(self):
        formatted_when = localtime(self.when).strftime('%d-%b-%Y %X')
        if self.success:
            formatted_success = "YES"
        else:
            formatted_success = "NO"

        return u'%s - %s- Success ?: %s ' % (self.word, formatted_when, formatted_success)

