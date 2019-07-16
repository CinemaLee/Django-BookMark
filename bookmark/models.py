from django.db import models

# Create your models here.
class Bookmark(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    url = models.URLField('url', unique=True)

    def __str__(self):
        return self.title

    class Meta:
        # db_table = 'Practice_bookmark' # 기본 테이블 셋팅 이름은 bookmark_bookmark 앱_모델이름
        verbose_name_plural = '북마크'