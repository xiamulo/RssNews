from django.db import models

# Create your models here.
import mongoengine


class sites(mongoengine.Document):
    task_id = mongoengine.StringField(max_length=33)
    _id = mongoengine.StringField(max_length=2000)
    key = mongoengine.StringField(max_length=2000)
    title = mongoengine.StringField(max_length=2000)
    img_url = mongoengine.StringField(max_length=2000)
    content = mongoengine.StringField(max_length=2000)
    datetime = mongoengine.StringField(max_length=2000)
    link = mongoengine.StringField(max_length=2000)
    author = mongoengine.StringField(max_length=2000)
    creattime = mongoengine.StringField(max_length=2000)
    keyword = mongoengine.StringField(max_length=2000)

    class Meta:
        db_table = "sites"


class label(models.Model):
    labelname = models.CharField(max_length=200)
    type = models.CharField(max_length=200)

    class Meta:
        db_table = "label"
