# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attempt',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('when', models.DateTimeField(auto_now_add=True)),
                ('success', models.BooleanField()),
            ],
            options={
                'ordering': ['-when'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Learner',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('username', models.CharField(max_length=30, null=True)),
                ('chosen_name', models.CharField(max_length=30)),
                ('family_name', models.CharField(max_length=30)),
                ('learning_level', models.IntegerField(default=0)),
            ],
            options={
                'ordering': ['family_name', 'chosen_name'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('user', models.OneToOneField(primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('chosen_name', models.CharField(max_length=30)),
                ('family_name', models.CharField(max_length=30)),
            ],
            options={
                'ordering': ['family_name', 'chosen_name'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Word',
            fields=[
                ('level', models.IntegerField()),
                ('word', models.CharField(max_length=30, unique=True, serialize=False, primary_key=True)),
                ('source', models.CharField(default=b'OT', max_length=2, choices=[(b'EW', b'Essential Words'), (b'ER', b'NZCER'), (b'OT', b'OTHER')])),
                ('hint', models.CharField(max_length=30, null=True, blank=True)),
            ],
            options={
                'ordering': ['level', 'word'],
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='learner',
            name='teacher',
            field=models.ForeignKey(to='spellweb.Teacher'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='attempt',
            name='learner',
            field=models.ForeignKey(to='spellweb.Learner'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='attempt',
            name='word',
            field=models.ForeignKey(to='spellweb.Word'),
            preserve_default=True,
        ),
    ]
