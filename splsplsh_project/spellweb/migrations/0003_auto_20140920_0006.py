# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('spellweb', '0002_auto_20140919_2143'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='attempt',
            name='learner',
        ),
        migrations.RemoveField(
            model_name='attempt',
            name='word',
        ),
        migrations.DeleteModel(
            name='Attempt',
        ),
        migrations.DeleteModel(
            name='Word',
        ),
    ]
