# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('twitter', '0002_tweet_msg'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hash',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ret', models.PositiveIntegerField()),
                ('fav', models.PositiveIntegerField()),
                ('fore', models.ForeignKey(to='twitter.Tweet')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
