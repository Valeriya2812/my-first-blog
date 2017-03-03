# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='article_image',
            field=models.ImageField(upload_to='images/', blank=True, null=True, verbose_name='Image'),
        ),
    ]
