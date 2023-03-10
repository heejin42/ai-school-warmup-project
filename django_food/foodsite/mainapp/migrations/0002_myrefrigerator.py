# Generated by Django 3.1.1 on 2020-09-17 15:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyRefrigerator',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('material', models.CharField(max_length=20, null=True)),
                ('food_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('shelf_life', models.IntegerField()),
                ('refrigerator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='refrigerator', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
