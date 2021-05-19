from django.db import models
from django.db.models.base import Model
from django.db.models.fields import URLField

class Tag(models.Model):
    slug = models.CharField(primary_key=True, unique=True, max_length=50)

    name =models.CharField(unique=True,max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self): 
        return self.slug


class Category(models.Model):
    name = models.CharField('カテゴリ名', max_length=50)
    name_en = models.CharField('カテゴリ名英語', max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def post_card(self):
        n = Card.objects.filter(category=self).count()
        return n

    def __str__(self):
        return self.name


class Card(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    color = models.CharField("色", max_length=5, choices=[("赤", "赤"), ("青", "青"), ("黄", "黄"), ("緑", "緑"), ("水", "水"), ("紫", "紫"),])
    url = models.URLField("URL",max_length=200,null=True,blank=True)
    title = models.CharField("タイトル",max_length=50)
    subtitle = models.TextField(
        "サブタイトル", max_length=300, null=True, blank=True)
    section = models.CharField("該当箇所", max_length=50, null=True, blank=True)
    content = models.TextField("本文",max_length=1000)
    what = models.TextField("何", max_length=200)
    why = models.TextField("理由", max_length=200)
    sowhat = models.TextField("だから何", max_length=200)
    tags = models.ManyToManyField(Tag, blank=True)



    def __str__(self):
        return self.title 
        # 管理画面でタイトル参照
    





