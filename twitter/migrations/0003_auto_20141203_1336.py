# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('twitter', '0002_tweet_msg'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hashtag',
            fields=[
                ('id_hastag', models.AutoField(serialize=False, primary_key=True)),
                ('nombre', models.CharField(default=b'', max_length=255)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='tweet',
            name='id',
        ),
        migrations.AddField(
            model_name='tweet',
            name='id_tweet',
            field=models.AutoField(default=1, serialize=False, primary_key=True),
            preserve_default=True,
        ),
    ]
