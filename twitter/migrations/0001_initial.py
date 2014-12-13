# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cadena',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(default=b'', max_length=255)),
            ],
            options={
                'verbose_name_plural': 'Cadena',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Ciudad',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(default=b'', max_length=255)),
            ],
            options={
                'verbose_name_plural': 'Ciudad',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Comida',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(default=b'', max_length=255)),
            ],
            options={
                'verbose_name_plural': 'Comida',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Contiene',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
                'verbose_name_plural': 'Contiene',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Evento',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha', models.DateTimeField(auto_now=True)),
                ('nombre', models.CharField(default=b'', max_length=255)),
                ('id_ciudad', models.ForeignKey(to='twitter.Cadena')),
            ],
            options={
                'verbose_name_plural': 'Evento',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Hashtag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(default=b'', max_length=255)),
                ('id_cadena', models.ForeignKey(to='twitter.Cadena')),
            ],
            options={
                'verbose_name_plural': 'Hashtag',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Menciona',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
                'verbose_name_plural': 'Menciona',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Pais',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(default=b'', max_length=255)),
            ],
            options={
                'verbose_name_plural': 'Pais',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Prepara',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('id_cadena', models.ForeignKey(to='twitter.Cadena')),
                ('id_comida', models.ForeignKey(to='twitter.Comida')),
            ],
            options={
                'verbose_name_plural': 'Prepara',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Referencia',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('id_comida', models.ForeignKey(to='twitter.Comida')),
                ('id_hashtag', models.ForeignKey(to='twitter.Hashtag')),
            ],
            options={
                'verbose_name_plural': 'Referencia',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Representa',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('id_cadena', models.ForeignKey(to='twitter.Cadena')),
            ],
            options={
                'verbose_name_plural': 'Representa',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Sigue',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('id_cadena', models.ForeignKey(to='twitter.Cadena')),
            ],
            options={
                'verbose_name_plural': 'Sigue',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Tweet',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('retweets', models.PositiveIntegerField()),
                ('favs', models.PositiveIntegerField()),
                ('msg', models.CharField(default=b'', max_length=255)),
            ],
            options={
                'verbose_name_plural': 'Tweet',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('seguidores', models.PositiveIntegerField()),
                ('cuenta', models.CharField(default=b'', max_length=255)),
                ('id_ciudad', models.ForeignKey(to='twitter.Ciudad')),
            ],
            options={
                'verbose_name_plural': 'Usuario',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='tweet',
            name='id_usuario',
            field=models.ForeignKey(to='twitter.Usuario'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='sigue',
            name='id_usuario',
            field=models.ForeignKey(to='twitter.Usuario'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='representa',
            name='id_usuario',
            field=models.ForeignKey(to='twitter.Usuario'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='menciona',
            name='id_tweet',
            field=models.ForeignKey(to='twitter.Tweet'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='menciona',
            name='id_usuario',
            field=models.ForeignKey(to='twitter.Usuario'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='contiene',
            name='id_hashtag',
            field=models.ForeignKey(to='twitter.Hashtag'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='contiene',
            name='id_tweet',
            field=models.ForeignKey(to='twitter.Tweet'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='ciudad',
            name='id_pais',
            field=models.ForeignKey(to='twitter.Pais'),
            preserve_default=True,
        ),
    ]
