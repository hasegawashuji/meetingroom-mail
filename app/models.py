from django.db import models
from accounts.models import CustomUser
from django.utils import timezone
import datetime



class Schedule(models.Model):
    """スケジュール"""
    summary = models.CharField('概要', max_length=50)
    description = models.TextField('詳細な説明', blank=True)
    start_time = models.TimeField('開始時間', default=datetime.time(7, 0, 0))
    end_time = models.TimeField('終了時間', default=datetime.time(7, 0, 0))
    date = models.DateField('日付')
    created_at = models.DateTimeField('作成日', default=timezone.now)

    def __str__(self):
        return self.summary




class Room(models.Model):
    name = models.CharField('会議室名', max_length=100)
    # r_date = models.ManyToManyField(Schedule, verbose_name='日付')
    description = models.TextField('説明', default='', blank=True)

    def __str__(self):
        return self.name


class Staff(models.Model):
    user = models.OneToOneField(CustomUser, verbose_name='スタッフ', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user}'


class Booking(models.Model):
    staff = models.ForeignKey(Staff, verbose_name='スタッフ', on_delete=models.CASCADE)
    room = models.ForeignKey(Room, verbose_name='会議室', on_delete=models.CASCADE)
    first_name = models.CharField('姓', max_length=100, null=True, blank=True)
    last_name = models.CharField('名', max_length=100, null=True, blank=True)
    remarks = models.TextField('備考', default='', blank=True)
    start = models.DateTimeField('開始時間', default=timezone.now)
    end = models.DateTimeField('終了時間', default=timezone.now)

    def __str__(self):
        start = timezone.localtime(self.start).strftime('%Y/%m/%d %H:%M')
        end = timezone.localtime(self.end).strftime('%Y/%m/%d %H:%M')

        return f'{self.first_name}{self.last_name} {start} ~ {end} {self.staff}'