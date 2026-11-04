---
title: "dmDjango 驱动"
book: "DM8 dmPython 使用手册"
version: "DM8"
source: https://eco.dameng.com/document/dm/zh-cn/pm/dmdjango-drive.html
tags:
  - dameng
  - dm8
  - dmpython
---

## 4.1 简介及安装

Django 是基于 Python 的 Web 应用程序框架， dmDjango 是 DM 提供的 Django 连接 DM 数据库的驱动，两者的版本对应关系如下：

表4.1 dmDjango版本对应表

| **dmDjango 版本** | **Django 版本** |
| --- | --- |
| dmDjango2.0.x | Django1.9、Django1.10、Django1.11、Django2.0、Django2.1、Django2.2、Django3.0 |
| dmDjango3.0.x | Django3.1、Django3.2、Django4.0、Django4.1 及以上版本 |

dmDjangon 可以运行在任何安装了 python 的平台上，可以使用安装包安装，也可以直接用源码安装。

可以使用如下命令很方便地在 Windows 和 Linux 操作系统下编译并安装 dmDjango:

```
//进入到setup.py所在的源码目录，执行以下命令：

python setup.py install
```

也可以先生成安装文件再进行安装。

在 Windows 操作系统下生成 exe 文件的操作如下，之后只需要直接执行 exe 文件即可安装：

```
//进入到setup.py所在的源码目录，执行以下命令：

python setup.py bdist_wininst
```

在 Linux 操作系统下使用 rpm 包安装 dmPython，生成 rpm 包的操作如下所示：

```
//进入到setup.py所在的源码目录，执行以下命令：

python setup.py bdist_rpm
```

安装和卸载命令参考如下：

```
安装：rpm -ivh dmDjango-1.0-1.noarch.rpm
卸载：rpm -e dmDjango-1.0-1.noarch.rpm
```

## 4.2 举例说明

### 4.2.1 创建 Django 项目

进入创建项目所在目录，例如 D:\\django\_dmPython，在该目录下使用如下命令创建 mysite 项目：

```
django-admin startproject mysite
```

Django 将会创建一个 mysite 目录，该目录包含 mysite 文件夹与 manage.py 文件。

### 4.2.2 数据库配置

Django 配置数据库默认为 sqlite3，这是一个小型数据库。要连接 DM 数据库，需修改 settings.py 中的 DATABASES 元组。配置方法如下：

```
DATABASES = {
    'default': {
        'ENGINE': 'dmDjango',
        'NAME': 'DAMENG',
        'USER': 'SYSDBA',
        'PASSWORD': 'Dmsys_123',
        'HOST': 'localhost',
        'PORT': '5236',
        'OPTIONS': {'local_code':1,'connection_timeout':5}
    }
}
```

OPTIONS：是各个驱动都支持的选项，只要在 OPTIONS 中以字典对象的方式配置 dmPython.connect 支持的选项即可，例如：'local\_code':1。可以包含多个字典对象，用逗号分隔。dmPython.connect 请参考 [3.1.1.1 dmPython.connect](dmpython-interface.md)

### 4.2.3 创建 dm 应用

在 Django 中，项目是一个网站使用的配置和应用的集合，一个项目可以包含很多个应用。例如，使用如下命令创建一个 dm 应用：

```
cd mysite
python manage.py startapp dm
```

### 4.2.4 创建模型

编辑 dm\\models.py 文件。

```
from django.db import models

# Create your models here.
class Book(models.Model):
    class Meta:
        db_table = 'PRODUCT'
    PRODUCTID = models.AutoField(primary_key=True,  db_column='PRODUCTID')
    NAME = models.CharField(max_length=100, null=True)
    AUTHOR = models.CharField(max_length=25, null=True)
    PUBLISHER = models.CharField(max_length=50, null=True)
    PUBLISHTIME = models.DateField(null=True)
    PRODUCTNO = models.CharField(max_length=25, null=True)
    SATETYSTOCKLEVEL = models.IntegerField(null=True)
    ORIGINALPRICE = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    NOWPRICE = models.DecimalField(max_digits=10, decimal_places=4, null=True)
    DISCOUNT = models.DecimalField(max_digits=2, decimal_places=1, null=True)
    DESCRIPTION = models.TextField(null=True)
    TYPE = models.CharField(max_length=5, null=True)
    PAPERTOTAL = models.IntegerField(null=True)
    WORDTOTAL = models.IntegerField(null=True)
    SELLSTARTTIME = models.DateField(null=True)
    SELLENDTIME = models.DateField( null=True)
```

同时需要在 settings.py 文件中的 INSTALLED\_APPS 中添加设置'dm.apps.DmConfig'，将 dm 应用安装到 Django 项目里。

### 4.2.5 进行数据迁移

在 D:\\django\_dmPython\\mysite 目录下打开命令行工具，执行以下命令，为模型的改变生成迁移文件：

```
python manage.py makemigrations dm
python manage.py migrate
```

### 4.2.6 对数据库进行操作

（1）在 dm 目录中新建一个 services.py 文件，在该文件中实现增、删、改、查四个基本操作。

```
from .models import Book
#查询操作
def fun_get_books():
    books = Book.objects.all() #返回QuerySet
    total_rows=books.count()
    print('查询到'+str(total_rows)+'条记录')
    for book in books:
        print(book.NAME, book.AUTHOR, book.PUBLISHER)
    print('')
#增加操作
def fun_insert_book():
    NewBook = Book()
    NewBook.NAME = '水浒传'
    NewBook.AUTHOR = '施耐庵，罗贯中'
    NewBook.PUBLISHER = '中华书局'
    NewBook.PUBLISHTIME = '2005-4-1'
    NewBook.PRODUCTNO = '9787101046137'
    NewBook.SATETYSTOCKLEVEL = '10'
    NewBook.ORIGINALPRICE = '19'
    NewBook.NOWPRICE = '14.3'
    NewBook.DISCOUNT = '7.5'
    NewBook.DESCRIPTION = '''
        《水浒传》是宋江起义故事在民间长期流传基础上产生出来的，吸收了民间文学的营养。
        《水浒传》是我国人民最喜爱的古典长篇白话小说之一。它产生于明代，是在宋、元以来有关水浒的故事、话本、戏曲的基础上，由作者加工整理、创作而成的。
         全书以宋江领导的农民起义为主要题材，艺术地再现了中国古代人民反抗压迫、英勇斗争的悲壮画卷。
         作品充分暴露了封建统治阶级的腐朽和残暴，揭露了当时尖锐对立的社会矛盾和“官逼民反”的残酷现实，成功地塑造了鲁智深、李逵、武松、林冲、阮小七等一批英雄人物。
         小说故事情节曲折，语言生动，人物性格鲜明，具有高度的艺术成就。但作品歌颂、美化宋江，鼓吹“忠义”和“替天行道”，表现出严重的思想局限。
        '''
    NewBook.PHOTO = ''
    NewBook.TYPE = '16'
    NewBook.PAPERTOTAL = '922'
    NewBook.WORDTOTAL = '912000'
    NewBook.SELLSTARTTIME = '2006-03-20'
    NewBook.SELLENDTIME = '2021-07-12'

    NewBook.save()
    print('插入成功')
#更新操作
def fun_update_book():
    try:
        obj = Book.objects.get(PRODUCTID=1)  #返回结果有且只有一个
        obj.NAME='水浒'
        obj.save()
        print('更新成功')
    except Book.DoesNotExist:
        print('PRODUCTID=1的记录不存在，未更新任何数据')
#删除操作
def fun_delete_book():
    obj = Book.objects.filter(NAME='水浒') #返回QuerySet
    del_rows=obj.count()
    obj.delete()
    print('删除'+str(del_rows)+'条记录')
```

（2）编写 dm\\views.py 文件。

```
from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse
from .services import fun_get_books
from .services import fun_insert_book
from .services import fun_update_book
from .services import fun_delete_book

def index(request):
    # 查询
    fun_get_books()

    # 增加
    fun_insert_book()
    fun_get_books()

    # 更新
    fun_update_book()
    fun_get_books()

    # 删除
    fun_delete_book()
    fun_get_books()
    return HttpResponse("执行结束，请到控制台查看输出结果。")
```

（3）在 dm 目录里新建 urls.py 文件。

```
from . import views
from django.urls import path
urlpatterns = [
    path('', views.index, name='index'),
]
```

（4）在 mysite\\urls.py 文件的 urlpatterns 列表中指定创建的 dm.urls 模块。

```
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('dm/',include('dm.urls')),
    path('admin/', admin.site.urls),
]
```

（5）在命令行工具中输入以下命令，启动 Django 自带的简易服务器：

```
python manage.py runserver
```

默认使用浏览器访问 http://127.0.0.1:8000/dm/，即可查看输出结果。

## 4.3 类型映射

Django 中的列类型通常使用 Field 指定，与数据库中的类型进行对应映射，dmDjango 支持当前 Django 的类型，类型映射对照关系如下：

表4.1 dmDjango版本对应表

| Django 类型 | 数据库类型 |
| --- | --- |
| SmallAutoField | INTEGER IDENTITY(1,1) |
| AutoField | INTEGER IDENTITY(1,1) |
| BigAutoField | BIGINT IDENTITY(1,1) |
| BinaryField | BLOB |
| BooleanField | TINYINT |
| CharField | VARCHAR(max\_length) |
| CommaSeparatedIntegerField | VARCHAR(max\_length) |
| DateField | DATE |
| DateTimeField | TIMESTAMP |
| DecimalField | NUMBER(max\_digits, decimal\_places) |
| DurationField | INTERVAL DAY(9) TO SECOND(6) |
| FileField | VARCHAR(max\_length) |
| FilePathField | VARCHAR(max\_length) |
| FloatField | DOUBLE PRECISION |
| IntegerField | INTEGER |
| BigIntegerField | BIGINT |
| IPAddressField | VARCHAR(15) |
| GenericIPAddressField | VARCHAR(39) |
| NullBooleanField | TINYINT |
| OneToOneField | INTEGER |
| PositiveIntegerField | INTEGER |
| PositiveBigIntegerField | BIGINT |
| PositiveSmallIntegerField | SMALLINT |
| SlugField | VARCHAR(max\_length) |
| SmallIntegerField | SMALLINT |
| TextField | TEXT |
| TimeField | TIMESTAMP |
| URLField | VARCHAR(max\_length) |
| UUIDField | VARCHAR(32) |
| JSONField | JSON |
| VectorField | VECTOR |

## 4.4 特殊说明

1. 按照 Django 规范，使用 dmDjango 创建的用户不会默认赋予 SOI 角色权限，因此新创建的用户默认无法访问 SYS 模式下的系统。
2. 创建连接时可以通过 OPTIONS 设置选项，在 dmDjango 中允许设置仅属于 dmDjango 的特殊的连接选项，不设置将采取默认值：empty\_string\_as\_null 选项可以设置为 True 或者 False，默认值为 False，此选项可以用来更改 char 类型以及其派生类型默认情况下的值，若设置为 True，在插入时不设置情况下将默认插入，若设置为 False，则将默认插入 NULL，其余情况将报错。
3. 由于 Django 暂时没有 VectorField 类型，因此在使用 VectorField 时需要从 dmDjango 中引入，插入删除等其余使用方法与正常类型相同。

## 4.5 方言包特殊连接参数

为了适配不同情况，创建连接时可以通过 OPTIONS 设置选项，在 dmDjango 中允许设置仅属于 dmDjango 的特殊的连接选项，当前 dmDjango 包含以下连接参数：

empty\_string\_as\_null 选项：

简介：用来更改 char 类型以及其派生类型默认情况下的值

可选值：true 或者 false

默认值：false

不同选项含义：若设置为 true，则默认插入空字符串''；若设置为 false，则默认插入 NULL，其余情况将报错。

compatible\_mode 选项：

简介：用来适配不同兼容模式下处理

可选值：0~8

默认值：0

不同选项含义：当前仅当参数值为 2 时会有区别，其余参数值对于结果无影响。当参数值为 2 兼容 ORACLE 时，无论数据库内部对于字符串返回为 NULL 还是空字符串，在 dmDjango 映射数据时都被返回为空字符串。