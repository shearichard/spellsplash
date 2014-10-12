from datetime import datetime

from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import localtime
from django.core.validators import MinValueValidator
from django.core.validators import MaxValueValidator

ESSENTIALWORDS = 'EW'
NZCER = 'ER'
OTHER = 'OT'
WORDSOURCE_TYPE_CHOICES = (
    (ESSENTIALWORDS, 'Essential Words'),
    (NZCER, 'NZCER'),
    (OTHER, 'OTHER'),
)

MIN_BOX_LEVEL=0
MAX_BOX_LEVEL=4

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
    starting_level = models.IntegerField(default=0)
    source = models.CharField(max_length=2,
                              choices=WORDSOURCE_TYPE_CHOICES,
                              default=ESSENTIALWORDS)

    class Meta:
        ordering = ['family_name', 'chosen_name']

    def __unicode__(self):
        return u'%s, %s' % (self.family_name, self.chosen_name)

class WordManager(models.Manager):
    def after_adding_boxes(self, curr_learner):
        '''
        Returns all `Word` objects for curr_learner
        at the relevant `learning_level`.

        Before it does that it first checks whether all
        corresponding `Box` obects exist and if they do
        not then it cretes them
        '''
        #All boxes for this Learner
        lst_extant_box_id_for_lrnr = Box.objects.filter(
                    learner=curr_learner
                ).values_list('word_id', flat=True)
        print lst_extant_box_id_for_lrnr


        #Every `Word` up to current level that, for this `Learner`,
        #that doesn't have a `Box`
        words_that_need_boxes = Word.objects.filter(
                    source=curr_learner.source
                ).filter(
                    level__lte=curr_learner.learning_level
                ).exclude(
                    id__in=lst_extant_box_id_for_lrnr
                )
        #Add a `Box` for each `Word` that doesn't have one
        lst_boxes = []
        for wrd in words_that_need_boxes:
            lst_boxes.append(Box(learner=curr_learner, word=wrd, box_number=MIN_BOX_LEVEL))

        print("About to insert {0} 'Boxes' for 'Learner' : {1}".format(len(lst_boxes), curr_learner))

        Box.objects.bulk_create(lst_boxes)

        #Now return the 'normal' `Word` QS
        wordQS = Word.objects.filter(
                    source=curr_learner.source
                ).filter(
                    level__lte=curr_learner.learning_level
                )

        return wordQS


class Word(models.Model):
    objects = WordManager()

    level = models.IntegerField()
    word = models.CharField(max_length=30)
    source = models.CharField(max_length=2,
                              choices=WORDSOURCE_TYPE_CHOICES,
                              default=ESSENTIALWORDS)
    hint = models.CharField(max_length=30, null=True, blank=True)

    class Meta:
        ordering = ['level', 'word']
        unique_together = (("source", "word"),)

    def __unicode__(self):
        return self.word

    

class Attempt(models.Model):
    '''
    `Attempt` represents an occassion when a `Learner`
    has been asked to spell a `Word`.

    The results and time of the `Attempt` are recorded
    '''
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


class Box(models.Model):
    '''
    `Box` represents a "Box" in the sense of the Leitner system of improving
    the use of flashcards.

    A predetermined number of boxes are used. If the `Learner` is able to
    correctly spell a `Word` the `Word` moves up to a higher level `Box`; 
    if they fail to spell a `Word` the `Word` moves down a level.

    When we are selecting a group of `Word` objects using the Leitner system
    words that appear in a lower level `Box` are more likely to be selected
    '''
    class Meta:
        verbose_name_plural = "Boxes"

    learner = models.ForeignKey(Learner)
    word = models.ForeignKey(Word)
    box_number = models.IntegerField(validators=[MinValueValidator(MIN_BOX_LEVEL), 
                                                 MaxValueValidator(MAX_BOX_LEVEL)])
