# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MeetingData',
            fields=[
                ('id', models.AutoField(verbose_name='Id', primary_key=True, serialize=False, help_text='Unique identifier')),
                ('user_name', models.CharField(verbose_name='User full name', max_length=256)),
                ('user_email', models.EmailField(verbose_name='User email', max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='MeetingDate',
            fields=[
                ('id', models.AutoField(verbose_name='Id', primary_key=True, serialize=False, help_text='Unique identifier')),
                ('date', models.DateField(verbose_name='Meeting date', unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='MeetingTime',
            fields=[
                ('id', models.AutoField(verbose_name='Id', primary_key=True, serialize=False, help_text='Unique identifier')),
                ('time_from', models.TimeField(verbose_name='Meeting begin time')),
                ('time_to', models.TimeField(verbose_name='Meeting end time')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='meetingtime',
            unique_together=set([('time_from', 'time_to')]),
        ),
        migrations.AddField(
            model_name='meetingdata',
            name='date',
            field=models.ForeignKey(verbose_name='Date', to='appointment.MeetingDate'),
        ),
        migrations.AddField(
            model_name='meetingdata',
            name='time',
            field=models.ForeignKey(verbose_name='Time', to='appointment.MeetingTime'),
        ),
    ]
