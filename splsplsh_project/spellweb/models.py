from django.db import models
from django.contrib.auth.models import User

class Teacher(models.Model):
    user = models.OneToOneField(User, primary_key=True)
    chosen_name = models.CharField(max_length=30)
    family_name = models.CharField(max_length=30)

    class Meta:
        ordering = ['family_name', 'chosen_name']

    def __unicode__(self):
            return self.user

class Learner(models.Model):
    teacher = models.ForeignKey(Teacher)
    chosen_name = models.CharField(max_length=30)
    family_name = models.CharField(max_length=30)
    learning_level = models.IntegerField(default=0)

    class Meta:
        ordering = ['family_name', 'chosen_name']

class Word(models.Model):
    level = models.IntegerField()
    word = models.CharField(primary_key=True, unique=True, max_length=30)

    class Meta:
        ordering = ['level', 'word']

class Attempt(models.Model):
    learner = models.ForeignKey(Learner)
    word = models.ForeignKey(Word)
    when = models.DateTimeField(auto_now_add=True)
    success = models.BooleanField()

    class Meta:
        ordering = ['-when']
    
