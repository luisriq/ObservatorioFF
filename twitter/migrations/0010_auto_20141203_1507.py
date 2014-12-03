# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('twitter', '0009_auto_20141203_1451'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cadena',
            options={'verbose_name_plural': 'Cadena'},
        ),
        migrations.AlterModelOptions(
            name='ciudad',
            options={'verbose_name_plural': 'Ciudad'},
        ),
        migrations.AlterModelOptions(
            name='comida',
            options={'verbose_name_plural': 'Comida'},
        ),
        migrations.AlterModelOptions(
            name='contiene',
            options={'verbose_name_plural': 'Contiene'},
        ),
        migrations.AlterModelOptions(
            name='evento',
            options={'verbose_name_plural': 'Evento'},
        ),
        migrations.AlterModelOptions(
            name='hashtag',
            options={'verbose_name_plural': 'Hashtag'},
        ),
        migrations.AlterModelOptions(
            name='menciona',
            options={'verbose_name_plural': 'Menciona'},
        ),
        migrations.AlterModelOptions(
            name='pais',
            options={'verbose_name_plural': 'Pais'},
        ),
        migrations.AlterModelOptions(
            name='prepara',
            options={'verbose_name_plural': 'Prepara'},
        ),
        migrations.AlterModelOptions(
            name='referencia',
            options={'verbose_name_plural': 'Referencia'},
        ),
        migrations.AlterModelOptions(
            name='representa',
            options={'verbose_name_plural': 'Representa'},
        ),
        migrations.AlterModelOptions(
            name='sigue',
            options={'verbose_name_plural': 'Sigue'},
        ),
        migrations.AlterModelOptions(
            name='tweet',
            options={'verbose_name_plural': 'Tweet'},
        ),
        migrations.AlterModelOptions(
            name='usuario',
            options={'verbose_name_plural': 'Usuario'},
        ),
    ]
