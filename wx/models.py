from django.db import models

# Create your models here.
import mongoengine


class wx(mongoengine.Document):
    _id = mongoengine.StringField(max_length=2000)
    article_time = mongoengine.StringField(max_length=2000)
    img_url = mongoengine.StringField(max_length=2000)
    title = mongoengine.StringField(max_length=2000)
    real_url = mongoengine.StringField(max_length=2000)
    nowtime = mongoengine.StringField(max_length=2000)
    content = mongoengine.StringField(max_length=2000)
    keyword = mongoengine.StringField(max_length=2000)
    redis_db = mongoengine.StringField(max_length=2000)
    account_name = mongoengine.StringField(max_length=2000)
    #keyword = mongoengine.StringField(max_length=2000)

    class Meta:
        db_table = "wx"


class wb(mongoengine.Document):
    _id = mongoengine.StringField(max_length=2000)
    name = mongoengine.StringField(max_length=2000)
    detal_url = mongoengine.StringField(max_length=2000)
    content = mongoengine.StringField(max_length=2000)
    image_url = mongoengine.StringField(max_length=2000)
    pubish_time = mongoengine.StringField(max_length=2000)
    user_url = mongoengine.StringField(max_length=2000)
    nowtime = mongoengine.StringField(max_length=2000)
    #keyword = mongoengine.StringField(max_length=2000)

    class Meta:
        db_table = "wb"


class kuan(mongoengine.Document):
    task_id = mongoengine.StringField(max_length=33)
    _id = mongoengine.StringField(max_length=2000)
    keys = mongoengine.StringField(max_length=2000)
    title = mongoengine.StringField(max_length=2000)
    img_url = mongoengine.StringField(max_length=2000)
    updateContent=mongoengine.StringField(max_length=2000)
    appTime=mongoengine.StringField(max_length=2000)
    creattime=mongoengine.StringField(max_length=2000)


    class Meta:
        db_table = "kuan"


class liqu(mongoengine.Document):
    task_id = mongoengine.StringField(max_length=33)
    _id = mongoengine.StringField(max_length=2000)
    keys = mongoengine.StringField(max_length=2000)
    title = mongoengine.StringField(max_length=2000)
    img_url = mongoengine.StringField(max_length=2000)
    url = mongoengine.StringField(max_length=2000)
    updateContent = mongoengine.StringField(max_length=2000)
    appTime = mongoengine.StringField(max_length=2000)
    creattime = mongoengine.StringField(max_length=2000)


    class Meta:
        db_table = "liqu"


class label(models.Model):
    labelname = models.CharField(max_length=200)
    type = models.CharField(max_length=200)
    redis_Name=models.CharField(max_length=200)

    class Meta:
        db_table = "label"
