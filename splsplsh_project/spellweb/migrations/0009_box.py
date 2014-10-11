# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('spellweb', '0008_auto_20140929_1910'),
    ]

    operations = [
        migrations.CreateModel(
            name='Box',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('box_number', models.IntegerField()),
                ('learner', models.ForeignKey(to='spellweb.Learner')),
                ('word', models.ForeignKey(to='spellweb.Word')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
