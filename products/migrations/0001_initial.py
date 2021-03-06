# Generated by Django 2.2.17 on 2021-02-16 15:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('url', models.URLField()),
                ('pub_date', models.DateTimeField()),
                ('votes_total', models.IntegerField(default=1)),
                ('image', models.ImageField(upload_to=None)),
                ('icon', models.ImageField(upload_to=None)),
                ('body', models.TextField(max_length=250)),
                ('hunter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
