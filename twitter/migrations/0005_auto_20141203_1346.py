# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('twitter', '0004_auto_20141203_1337'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hashtag',
            name='id_hastag',
        ),
        migrations.RemoveField(
            model_name='tweet',
            name='id_tweet',
        ),
        migrations.AddField(
            model_name='hashtag',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, default=1, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='hashtag',
            name='id_cadena',
            field=models.ForeignKey(default=11, to='twitter.Tweet'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tweet',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, default=365, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
    ]
