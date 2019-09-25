from django.db import models

# Create your models here.
# 书籍的类
class Book(models.Model):
    id = models.AutoField(primary_key=True)
    bookname = models.CharField(max_length=64,verbose_name='书名')
    book_type=models.CharField(max_length=64,verbose_name='书籍类型')
    book_word_counts=models.IntegerField(verbose_name='字数')
    is_hot_sale=models.BooleanField(verbose_name='是否热售')
    class Meta:
        db_table='book'
        verbose_name = '书'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.bookname