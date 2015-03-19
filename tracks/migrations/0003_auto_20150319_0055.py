# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tracks', '0002_auto_20150313_2326'),
    ]

    operations = [
        migrations.RenameField(
            model_name='track',
            old_name='track_field',
            new_name='track_file',
        ),
    ]
