# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('spellweb', '0003_auto_20140920_0006'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attempt',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('when', models.DateTimeField(auto_now_add=True)),
                ('success', models.BooleanField(default=False)),
                ('learner', models.ForeignKey(to='spellweb.Learner')),
            ],
            options={
                'ordering': ['-when'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Word',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('level', models.IntegerField()),
                ('word', models.CharField(max_length=30)),
                ('source', models.CharField(default=b'OT', max_length=2, choices=[(b'EW', b'Essential Words'), (b'ER', b'NZCER'), (b'OT', b'OTHER')])),
                ('hint', models.CharField(max_length=30, null=True, blank=True)),
            ],
            options={
                'ordering': ['level', 'word'],
            },
            bases=(models.Model,),
        ),
        migrations.AlterUniqueTogether(
            name='word',
            unique_together=set([('source', 'word')]),
        ),
        migrations.AddField(
            model_name='attempt',
            name='word',
            field=models.ForeignKey(to='spellweb.Word'),
            preserve_default=True,
        ),
    ]
