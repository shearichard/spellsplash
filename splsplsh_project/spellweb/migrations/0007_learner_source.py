# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('spellweb', '0006_learner_starting_level'),
    ]

    operations = [
        migrations.AddField(
            model_name='learner',
            name='source',
            field=models.CharField(default=b'OT', max_length=2, choices=[(b'EW', b'Essential Words'), (b'ER', b'NZCER'), (b'OT', b'OTHER')]),
            preserve_default=True,
        ),
    ]
