from django.db import models
import apps.user.models

# Create your models here.


class BBS(models.Model):
    title = models.CharField(max_length=64)
    content = models.TextField()
    author = models.ForeignKey('user.UserProfile', on_delete=models.CASCADE)
    category = models.CharField(max_length=32, default='01')
    view_count = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.title


class CatgoryName(models.Model):
    cat_id = models.CharField(max_length=3)
    cat_name = models.CharField(max_length=32)


class Reply(models.Model):
    content = models.CharField(max_length=600)
    author = models.ForeignKey('user.UserProfile', on_delete=models.CASCADE)
    thread = models.ForeignKey('BBS', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
