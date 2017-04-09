from django.db import models
from django.utils import formats


class MeetingDate(models.Model):
    id = models.AutoField(primary_key=True, verbose_name='Id', help_text='Unique identifier')
    date = models.DateField('Meeting date', unique=True)

    def __str__(self):
        return self.date.strftime('%d %B %Y')


class MeetingTime(models.Model):
    id = models.AutoField(primary_key=True, verbose_name='Id', help_text='Unique identifier')
    time_from = models.TimeField('Meeting begin time')
    time_to = models.TimeField('Meeting end time')

    def __str__(self):
        return str.format(
            '{0} - {1}',
            formats.date_format(self.time_from, "TIME_FORMAT"),
            formats.date_format(self.time_to, "TIME_FORMAT")
        )


    class Meta:
        unique_together = ('time_from', 'time_to')


class MeetingData(models.Model):
    id = models.AutoField(primary_key=True, verbose_name='Id', help_text='Unique identifier')
    date=models.ForeignKey(MeetingDate, verbose_name='Date')
    time=models.ForeignKey(MeetingTime, verbose_name='Time')
    user_name=models.CharField(max_length=256, verbose_name='User full name')
    user_email=models.EmailField(max_length=254, verbose_name='User email')

    def __str__(self):
        return str.format(
            '{0}:{1} {2}:{3}',
            'User name',
            self.user_name,
            'Date',
            formats.date_format(self.date.date, "SHORT_DATE_FORMAT")
        )
