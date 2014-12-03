# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('twitter', '0005_auto_20141203_1346'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('seguidores', models.PositiveIntegerField()),
                ('cuenta', models.CharField(default=b'', max_length=255)),
                ('id_ciudad', models.ForeignKey(to='twitter.Hashtag')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
