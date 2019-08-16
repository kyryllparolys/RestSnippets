# Generated by Django 2.2.4 on 2019-08-13 09:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0005_auto_20190813_0905'),
    ]

    operations = [
        migrations.AlterField(
            model_name='info',
            name='owner',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='info', to=settings.AUTH_USER_MODEL),
        ),
    ]