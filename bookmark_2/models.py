from django.db import models

# Create your models here.
class Bookmark(models.Model):
    site_name = models.CharField(max_length=30, verbose_name = '사이트 이름')
    url = models.URLField()
    content = models.TextField(blank=True, verbose_name='사이트 설명')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.site_name

    class Meta:
        ordering = ['-created_at'] # 정렬순서 역순으로 구현.