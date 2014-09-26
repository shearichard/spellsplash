# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('spellweb', '0005_auto_20140923_2219'),
    ]

    operations = [
        migrations.AddField(
            model_name='learner',
            name='starting_level',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
