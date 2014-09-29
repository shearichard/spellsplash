# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('spellweb', '0007_learner_source'),
    ]

    operations = [
        migrations.AlterField(
            model_name='learner',
            name='source',
            field=models.CharField(default=b'EW', max_length=2, choices=[(b'EW', b'Essential Words'), (b'ER', b'NZCER'), (b'OT', b'OTHER')]),
        ),
        migrations.AlterField(
            model_name='word',
            name='source',
            field=models.CharField(default=b'EW', max_length=2, choices=[(b'EW', b'Essential Words'), (b'ER', b'NZCER'), (b'OT', b'OTHER')]),
        ),
    ]
