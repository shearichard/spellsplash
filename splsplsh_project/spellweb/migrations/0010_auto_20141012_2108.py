# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('spellweb', '0009_box'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='box',
            options={'verbose_name_plural': 'Boxes'},
        ),
        migrations.AlterField(
            model_name='box',
            name='box_number',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(4)]),
        ),
    ]
