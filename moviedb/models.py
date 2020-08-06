from django.db import models

# Create your models here.

class Movie(models.Model):
    """"映画リスト"""
    disk = models.IntegerField(verbose_name="ディスク番号",blank=True, null=True)
    title = models.CharField(verbose_name="タイトル", max_length=100)
    overview = models.CharField(verbose_name="概説",max_length=100)
    explain = models.CharField(verbose_name="解説",max_length=800)
    viewed_at = models.DateField(verbose_name='視聴日', blank=True, null=True)
    recorded_at = models.DateField(verbose_name='録画日',blank=True, null=True)
    media = models.CharField(verbose_name='メディア', max_length=50, blank=True, null=True)
    genre = models.CharField(verbose_name='ジャンル', max_length=50, blank=True)
    def __str__(self):
        return self.title


