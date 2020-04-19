from django.db import models
from django.urls import reverse

class Category(models.Model):
    name = models.CharField('商品名',max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = '分类'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_list_by_category', args=[self.slug])


class Product(models.Model):
    category = models.ForeignKey(Category, related_name='分类', on_delete=models.CASCADE)
    name = models.CharField('商品名称', max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)
    image = models.ImageField('商品图片',upload_to='products/%y/%m/%d', blank=True)
    description = models.TextField('商品描述',blank=True)
    price = models.DecimalField('价格',max_digits=10, decimal_places=2)
    available = models.BooleanField('是否可以购买',default=True)
    created = models.DateTimeField('创建时间',auto_now_add=True)
    updated = models.DateTimeField('更新时间',auto_now=True)

    class Meat:
        verbose_name = "商品"
        verbose_name_plural = verbose_name
        ordering = ('name',)
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_detail', args=[self.id, self.slug])