# _*_ coding:utf-8 _*_
from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()
    sex = models.CharField(max_length=1,choices=[('1',u'男'),('2',u'女')],default=('1',u'男'))
    books = models.ManyToManyField('Book', null=True, blank=True)
    
    def __unicode__(self):
        return u"名字: %s----年龄: %d" % (self.name, self.age)

class Book(models.Model):
    name = models.CharField(max_length=30)
    price = models.FloatField()

    def __unicode__(self):
        return u"名字: %s 价格: %6.2f" % (self.name, self.price)