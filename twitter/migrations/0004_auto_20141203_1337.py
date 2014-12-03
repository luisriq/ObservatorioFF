# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('twitter', '0003_auto_20141203_1336'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweet',
            name='id_tweet',
            field=models.AutoField(serialize=False, primary_key=True),
            preserve_default=True,
        ),
    ]
